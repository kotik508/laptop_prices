import pandas as pd
import scrapy


class AlzaNotebookSpider(scrapy.Spider):
    name = "alza_pavouk"
    allowed_domains = ['alza.cz']
    start_urls = ['https://www.alza.cz/herni-notebooky/18848814.htm']
    notebooky = []

    def start_request(self):
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        notebooks = response.css('div.fb')
        for notebook in notebooks:
            links_to_follow = self.start_urls[0] + notebook.xpath('./a/@href').extract_first()
            yield response.follow(url=links_to_follow, callback=self.parse_notebooks)

    def parse_notebooks(self, response):
        block = response.xpath('//a[@class="last spec-item"]/text()').extract_first()
        self.notebooky.append(block)
        # for notebook in block:
        #     notebook_names = notebook.xpath('./text()').extract_first()


        # notebooks_ram = response.xpath('//div[@class="cell1"][2]/span[@class="value"]/text()')
        # notebooks_ram_ext = notebooks_ram.extract()
        # notebooks_cpu = response.xpath('//div[@class="cell1"][3]/span[@class="value"]/text()')
        # notebooks_cpu_ext = notebooks_cpu.extract()
        # notebooks_storage = response.xpath('//div[@class="cell1"][6]/span[@class="value"]/text()')
        # notebooks_storage_ext = notebooks_storage.extract()
        # notebooks_resolution = response.xpath('//div[@class="cell1"][9]/span[@class="value"]/text()')
        # notebooks_resolution_ext = notebooks_resolution.extract()
        # notebooks_ref_rate = response.xpath('//div[@class="cell1"][13]/span[@class="value"]/text()')
        # notebooks_ref_rate_ext = notebooks_ref_rate.extract()
        # notebooks_gpu = response.xpath('//div[@class="cell1"][28]/span[@class="value"]/text()')
        # notebooks_gpu_ext = notebooks_gpu.extract()
        # notebooks_price = response.css('span.price-box__price::text')
        # notebooks_price_ext = notebooks_price.extract()

        #     yield {
        #         "name": notebooks_names,
        #     # "RAM": notebooks_ram_ext,
        #     # "CPU": notebooks_cpu_ext,
        #     # "Storage": notebooks_storage_ext,
        #     # "Resolution": notebooks_resolution_ext,
        #     # "Refresh rate": notebooks_ref_rate_ext,
        #     # "GPU": notebooks_gpu_ext,
        #     # "Price": notebooks_price_ext
        # }