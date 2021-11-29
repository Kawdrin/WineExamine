from parsel import Selector
import requests


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
            self.htmls.append('https://www.wine.com.br'+html)

        proxima_pagina = html_seletor.xpath('//div[@class="Pagination"]//a')
        for pagina in proxima_pagina:
            if pagina.xpath('./text()').get() == "Próxima >>":
                self.coletar_site(f"https://www.wine.com.br{pagina.xpath('./@href').get().strip()}")

class ScrapingDados:
    def __init__(self, lista_htmls):
        self.lista_htmls = lista_htmls

        for html in lista_htmls:
            self.coletar_dados_site(html)

    def coletar_dados_site(self, site):
        html_text = requests.get(site).text

        html_seletor = Selector(text=html_text)
        nome = html_seletor.xpath('//h1/text()').get()
        tipo = html_seletor.xpath('//ul[@class="PageHeader-tags"]//li[2]/text()').get()
        textura = html_seletor.xpath('//ul[@class="PageHeader-tags"]//li[3]/text()').get()
        premios = html_seletor.xpath('//div[@class="Awards"][1]//span[@class="AwardsTrophy-text w-micro"][1]/text()').get()
        if premios == None:
            premios = 0
        pais = html_seletor.xpath('/html/body/div[10]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/dd/text()').get()
        safra = html_seletor.xpath('/html/body/div[10]/div[2]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/dd/text()').get()
        html = site




ScrapingDados(['https://www.wine.com.br/vinhos/william-hill-central-coast-chardonnay-2017/prod23645.html'])
