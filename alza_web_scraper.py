import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
import numpy as np


class AlzaNotebookSpider(scrapy.Spider):

    name="alza_pavouk"
    url_alza="https://www.alza.cz/herni-notebooky/18848814.htm"
    df_laptop = pd.DataFrame(columns=["Name", "RAM", "CPU", "Storage", "Resolution", "Refresh Rate", "GPU", "Price"])

    def start_request(self):
        yield scrapy.Request(url=url_alza, callback=self.parse)

    def parse(self, response):
        notebooks = response.css('div.fb')
        notebooks_links = notebooks.xpath('./a/@href')
        links_to_follow = notebooks_links.extract()
        for url in links_to_follow:
            yield response.follow(url=url, callback=self.parse_notebooks)

    def parse_notebooks(self,response):
        notebooks_names = response.xpath('//h1[@itemprop="name"]/text()')
        notebooks_names_ext = notebooks_names.extract().strip()
        notebooks_ram = response.xpath('//div[@class="cell1"][2]/span[@class="value"]/text()')
        notebooks_ram_ext = notebooks_ram.extract().strip()
        notebooks_cpu = response.xpath('//div[@class="cell1"][3]/span[@class="value"]/text()')
        notebooks_cpu_ext = notebooks_cpu.extract().strip()
        notebooks_storage = response.xpath('//div[@class="cell1"][6]/span[@class="value"]/text()')
        notebooks_storage_ext = notebooks_storage.extract().strip()
        notebooks_resolution = response.xpath('//div[@class="cell1"][9]/span[@class="value"]/text()')
        notebooks_resolution_ext = notebooks_resolution.extract().strip()
        notebooks_ref_rate = response.xpath('//div[@class="cell1"][13]/span[@class="value"]/text()')
        notebooks_ref_rate_ext = notebooks_ref_rate.extract().strip()
        notebooks_gpu = response.xpath('//div[@class="cell1"][28]/span[@class="value"]/text()')
        notebooks_gpu_ext = notebooks_gpu.extract().strip()
        notebooks_price = response.css('span.price-box__price::text')
        notebooks_price_ext = notebooks_price.extract().strip()

        df_laptop.loc[len(df_laptop.index)] = [notebooks_names_ext, notebooks_ram_ext, notebooks_cpu_ext,
                                               notebooks_storage_ext, notebooks_resolution_ext, notebooks_ref_rate_ext,
                                               notebooks_gpu_ext, notebooks_price_ext]




