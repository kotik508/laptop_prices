import scrapy


class AlzaNotebookSpider(scrapy.Spider):
    name = "alza_pavouk"
    allowed_domains = ['alza.cz']
    start_urls = ['https://www.alza.cz/herni-notebooky/18848814.htm']

    def start_request(self):
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        notebooks_names = response.xpath('//a[@class="name browsinglink"]/text()').get
        yield {
            'names': notebooks_names
        }

        # notebooks = response.css('div.fb')
        # notebooks_links = notebooks.xpath('./a/@href')
        # links_to_follow = notebooks_links.extract()

        #for url in links_to_follow:
        #    yield response.follow(url=url, callback=self.parse_notebooks)

    # def parse_notebooks(self,response):
    #     notebooks_names = response.xpath('//h1[@itemprop="name"]/text()')
    #     notebooks_names_ext = notebooks_names.extract()
    #     notebooks_ram = response.xpath('//div[@class="cell1"][2]/span[@class="value"]/text()')
    #     notebooks_ram_ext = notebooks_ram.extract()
    #     notebooks_cpu = response.xpath('//div[@class="cell1"][3]/span[@class="value"]/text()')
    #     notebooks_cpu_ext = notebooks_cpu.extract()
    #     notebooks_storage = response.xpath('//div[@class="cell1"][6]/span[@class="value"]/text()')
    #     notebooks_storage_ext = notebooks_storage.extract()
    #     notebooks_resolution = response.xpath('//div[@class="cell1"][9]/span[@class="value"]/text()')
    #     notebooks_resolution_ext = notebooks_resolution.extract()
    #     notebooks_ref_rate = response.xpath('//div[@class="cell1"][13]/span[@class="value"]/text()')
    #     notebooks_ref_rate_ext = notebooks_ref_rate.extract()
    #     notebooks_gpu = response.xpath('//div[@class="cell1"][28]/span[@class="value"]/text()')
    #     notebooks_gpu_ext = notebooks_gpu.extract()
    #     notebooks_price = response.css('span.price-box__price::text')
    #     notebooks_price_ext = notebooks_price.extract()







