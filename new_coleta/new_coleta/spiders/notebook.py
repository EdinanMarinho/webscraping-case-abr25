import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/forno-eletrico?sb=rb#D[A:forno%20eletrico]"]

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:

            yield {
                'brand':product.css('span.poly-component__brand::text').get()
            }

        pass
