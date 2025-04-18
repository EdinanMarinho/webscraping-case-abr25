import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/forno-eletrico?sb=rb#D[A:forno%20eletrico]"]

    def parse(self, response):
        pass
