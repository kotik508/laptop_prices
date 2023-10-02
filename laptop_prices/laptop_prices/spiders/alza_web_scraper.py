import pandas as pd
import scrapy


class AlzaNotebookSpider(scrapy.Spider):
    name = "alza_pavouk"
    allowed_domains = ['alza.cz']
    start_urls = ['https://www.alza.cz/herni-notebooky/18848814.htm']

    def start_request(self):
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        notebooks = response.css('div.fb')
        for notebook in notebooks:
            links_to_follow = self.start_urls[0] + notebook.xpath('./a/@href').extract_first() + "#parametry"
            yield response.follow(url=links_to_follow, callback=self.parse_notebooks)

    def parse_notebooks(self, response):
        top_table = response.xpath('//div[contains(@class, "groupValues js-top-parameters")]/div[contains(@class, "row")]/span[@class="value"]/text()')
        table = response.xpath('//div[@class="container params"]')
        name = response.xpath('//a[contains(@class, "last")]/text()').extract_first()
        notebooks_ram = top_table.extract()[1]
        notebooks_cpu = top_table.extract()[2]
        notebooks_storage = top_table.extract()[5]
        notebooks_resolution = table.xpath('.//div[contains(@class, "row")][7]/span[@class="value"]/text()').extract_first()
        notebooks_ref_rate = table.xpath('.//div[contains(@class, "row")][13]/span[@class="value"]/text()').extract_first()
        notebooks_gpu = table.xpath('.//div[contains(@class, "row")][28]/span[@class="value"]/text()').extract_first()
        notebooks_price = response.css('span.price-box__price::text').extract_first()


        yield {
            "name": name,
            "RAM": notebooks_ram,
            "CPU": notebooks_cpu,
            "Storage": notebooks_storage,
            "Resolution": notebooks_resolution,
            "Refresh rate": notebooks_ref_rate,
            "GPU": notebooks_gpu,
            "Price": notebooks_price
        }