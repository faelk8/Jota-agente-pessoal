from loguru import logger
from src.inovacao_tecnologica.coletar_links import InovacaoTecnologicaScraper
from src.inovacao_tecnologica.coletar_noticia import InovacaoTecnologicaNoticia


scraper = InovacaoTecnologicaScraper(
    'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=materiais'
)

links = scraper.coletar_links()

caminho_pasta = '/home/rafael/Documentos/github/agente/data/noticias/inovacao-tecnologica/materias'

total = len(links)
checkpoints = {int(total * i / 10) for i in range(1, 11)}

for i, link in enumerate(links, start=1):
    noticia = InovacaoTecnologicaNoticia(link, caminho_pasta)
    noticia.coletar_dados()

    if i in checkpoints:
        progresso = int(i / total * 100)
        logger.info(f"{progresso}% concluído")

####################################################################################################################################

scraper = InovacaoTecnologicaScraper(
    'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=mecanica'
)

links = scraper.coletar_links()

caminho_pasta = '/home/rafael/Documentos/github/agente/data/noticias/inovacao-tecnologica/mecanica'

total = len(links)
checkpoints = {int(total * i / 10) for i in range(1, 11)}

for i, link in enumerate(links, start=1):
    noticia = InovacaoTecnologicaNoticia(link, caminho_pasta)
    noticia.coletar_dados()

    if i in checkpoints:
        progresso = int(i / total * 100)
        logger.info(f"{progresso}% concluído")


####################################################################################################################################

scraper = InovacaoTecnologicaScraper(
    'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=meio-ambiente'
)

links = scraper.coletar_links()

caminho_pasta = '/home/rafael/Documentos/github/agente/data/noticias/inovacao-tecnologica/meio-ambiente'

total = len(links)
checkpoints = {int(total * i / 10) for i in range(1, 11)}

for i, link in enumerate(links, start=1):
    noticia = InovacaoTecnologicaNoticia(link, caminho_pasta)
    noticia.coletar_dados()

    if i in checkpoints:
        progresso = int(i / total * 100)
        logger.info(f"{progresso}% concluído")


####################################################################################################################################

scraper = InovacaoTecnologicaScraper(
    'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=nanotecnologia'
)

links = scraper.coletar_links()

caminho_pasta = '/home/rafael/Documentos/github/agente/data/noticias/inovacao-tecnologica/nanotecnologia'

total = len(links)
checkpoints = {int(total * i / 10) for i in range(1, 11)}

for i, link in enumerate(links, start=1):
    noticia = InovacaoTecnologicaNoticia(link, caminho_pasta)
    noticia.coletar_dados()

    if i in checkpoints:
        progresso = int(i / total * 100)
        logger.info(f"{progresso}% concluído")


####################################################################################################################################

scraper = InovacaoTecnologicaScraper(
    'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=robotica'
)

links = scraper.coletar_links()

caminho_pasta = '/home/rafael/Documentos/github/agente/data/noticias/inovacao-tecnologica/robotica'

total = len(links)
checkpoints = {int(total * i / 10) for i in range(1, 11)}

for i, link in enumerate(links, start=1):
    noticia = InovacaoTecnologicaNoticia(link, caminho_pasta)
    noticia.coletar_dados()

    if i in checkpoints:
        progresso = int(i / total * 100)
        logger.info(f"{progresso}% concluído")
