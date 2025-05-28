from bs4 import BeautifulSoup
import requests
import re
import json
import unicodedata
import os
from loguru import logger


class InovacaoTecnologicaNoticia:
    def __init__(self, url, caminho_pasta):
        self.url = url
        self.caminho_pasta = caminho_pasta

    def _normalizar_texto(self, texto):
        texto = texto.lower()
        texto = unicodedata.normalize('NFKD', texto).encode(
            'ASCII', 'ignore').decode('ASCII')
        texto = re.sub(r'\s+', '-', texto)
        # Remove caracteres que não são letra, número ou hífen
        texto = re.sub(r'[^\w\-]', '', texto)
        return texto

    def coletar_dados(self):
        html = requests.get(self.url).content
        soup = BeautifulSoup(html, 'html.parser')

        # Seção
        secao = soup.find('div', class_='secao')
        secao = secao.get_text(strip=True) if secao else None

        # Título
        titulo = soup.find('h1')
        titulo = titulo.get_text(strip=True) if titulo else None

        # Fonte e data
        autor_data = soup.find('p', class_='suave')
        if autor_data:
            autor_data_text = autor_data.get_text(strip=True)

            # Expressão regular para separar fonte e data com hífen colado ou com espaços
            match = re.match(
                r'^(.*?)[\s\-–]+(\d{2}/\d{2}/\d{4})$', autor_data_text)
            if match:
                fonte, data = match.group(1).strip(), match.group(2)
            else:
                fonte, data = autor_data_text, None
        else:
            fonte, data = None, None

        # Legenda
        legenda_div = soup.find('div', class_='legenda')
        if legenda_div:
            legenda_texto = legenda_div.get_text(separator=' ', strip=True)
            legenda = legenda_texto.split('[Imagem:')[0].strip()
        else:
            legenda = None

        paragrafos = soup.find_all('p')

        texto_noticia = []
        for p in paragrafos:
            txt = p.get_text(strip=True)
            if (
                not txt or
                "redação do site inovação tecnológica" in txt.lower() or
                "mais tópicos" in txt.lower()
            ):
                continue
            texto_noticia.append(txt)

        texto_final = '\n\n'.join(texto_noticia)

        div_biblio = soup.find('div', class_='biblio')
        try:
            # Separa o texto por linhas removendo espaços extras
            linhas = [linha.strip() for linha in div_biblio.get_text(
                separator='\n').split('\n') if linha.strip()]

            # Inicializa variáveis
            autores = None
            revista = None

            # Percorre as linhas para encontrar autores e revista
            for linha in linhas:
                if linha.startswith('Autores:'):
                    autores = linha.replace('Autores:', '').strip()
                elif linha.startswith('Revista:'):
                    revista = linha.replace('Revista:', '').strip()

            arquivo = {
                "Origem": "Inovação Tecnológica",
                "Tipo": secao,
                "Título": titulo,
                "Fonte": fonte,
                "Data": data,
                "Legenda": legenda,
                "Texto": texto_final,
                "Autor": autores,
                "Publicação": revista
            }

            nome_arquivo = self._normalizar_texto(
                titulo) if titulo else 'arquivo'

            # Garantindo que a pasta exista
            os.makedirs(self.caminho_pasta, exist_ok=True)

            # Salva arquivo JSON
            caminho_arquivo = f"{self.caminho_pasta.rstrip('/')}/{nome_arquivo}.json"
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(arquivo, f, ensure_ascii=False, indent=4)

        except Exception as e:
            logger.error(f"Erro ao coletar dados da noticia: {e}")
