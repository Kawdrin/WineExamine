from parsel import Selector
import requests
import sqlite3

class ScrapingHTMLS:
    def __init__(self):
        self.htmls = []
        self.coletar_site('https://www.wine.com.br/vinhos/cVINHOS-p1.html')

    def get_htmls(self):
        return self.htmls

    def coletar_site(self, site):
        html_text = requests.get(site).text

        html_seletor = Selector(text=html_text)

        produtos = html_seletor.xpath('//div[@class="ProductList-content"]//li')
        for produto in produtos:
            html = produto.xpath('./article/a[@class="js-productClick"]/@href').get()
            nome = produto.xpath('.//h2/text()').get()
            if "Kit" not in nome and "Bag In Box" not in nome:
                self.htmls.append('https://www.wine.com.br'+html)

        proxima_pagina = html_seletor.xpath('//div[@class="Pagination"]//a')
        for pagina in proxima_pagina:
            if pagina.xpath('./text()').get() == "Próxima >>":
                self.coletar_site(f"https://www.wine.com.br{pagina.xpath('./@href').get().strip()}")

class ScrapingDados:
    def __init__(self, lista_htmls):
        self.lista_htmls = lista_htmls

        self.banco = sqlite3.connect("res/vinhos.db")

        self.cursor = self.banco.cursor()

        for html in lista_htmls:
            self.coletar_dados_site(html)
        self.cursor.execute("SELECT * FROM vinhos")

    def coletar_dados_site(self, site):
        html_text = requests.get(site).text

        html_seletor = Selector(text=html_text)
        nome = html_seletor.xpath('//h1/text()').get()
        nome = nome.replace("\'", '')
        nome = nome.replace('\"', '')
        tipo = html_seletor.xpath('//ul[@class="PageHeader-tags"]//li[2]/text()').get()
        textura = html_seletor.xpath('//ul[@class="PageHeader-tags"]//li[3]/text()').get()
        textura.replace("'", '')
        premios = html_seletor.xpath('//div[@class="Awards"][1]//span[@class="AwardsTrophy-text w-micro"][1]/text()').get()
        if premios is None:
            premios = 0

        ficha = html_seletor.xpath('//div[@class="TechnicalDetails"]')[0]
        pais = ficha.xpath('//div[@class="TechnicalDetails"]//div[@class="col-md-12 TechnicalDetails-description"][2]//dd/text()').get()
        pais = pais.replace("\'", '')
        pais = pais.replace('\"', '')
        safra = ficha.xpath('//div[@class="TechnicalDetails"]//div[@class="col-md-12 TechnicalDetails-description"][5]//dd/text()').get()
        if safra is None or len(safra) > 4:
            return None
        html = site
        try:
            self.cursor.execute(F"""INSERT INTO vinhos VALUES ("{nome}","{tipo}","{textura}","{premios}","{html}", "{pais}", "{safra}")""")
            self.banco.commit()
        except sqlite3.IntegrityError:
            return None


s = ScrapingHTMLS()
html_lista = s.get_htmls()
ScrapingDados(html_lista)
