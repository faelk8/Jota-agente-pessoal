import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from loguru import logger


class InovacaoTecnologicaScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.base_url_sem_base = base_url.split('&base=')[0]
        self.all_links = set()

    def coletar_links(self):
        base = 0
        incremento = 15

        while True:
            if base == 0:
                url = self.base_url_sem_base
            else:
                url = f"{self.base_url_sem_base}&base={base}"

            # logger.info(f"Buscando links na página: {url}")
            resp = requests.get(url)
            if resp.status_code != 200:
                logger.error("Erro na requisição ou página não encontrada.")
                break

            soup = BeautifulSoup(resp.text, 'html.parser')

            links = soup.find_all('a', href=True)

            links_validos = []
            for link in links:
                href = link['href']
                full_url = urljoin(
                    'https://www.inovacaotecnologica.com.br/noticias/', href)
                if '/noticia.php?artigo=' in full_url:
                    links_validos.append(full_url)

            if not links_validos:
                logger.error(
                    "Nenhum link válido encontrado nesta página, finalizando.")
                break

            before_count = len(self.all_links)
            self.all_links.update(links_validos)
            after_count = len(self.all_links)

            # print(f"Links coletados nesta página: {len(links_validos)} | Total acumulado: {after_count}")

            if before_count == after_count:
                logger.error(
                    "Nenhum link novo encontrado, finalizando a busca.")
                break

            base += incremento

        logger.info("\nTotal de links únicos coletados:", len(self.all_links))
        return sorted(self.all_links)
