from selenium import webdriver
import scrapy
import time


class AlzaNotebookSpider(scrapy.Spider):
    name = "alza_pavouk"
    allowed_domains = ['alza.cz']
    start_urls = ['https://www.alza.cz/herni-notebooky/18848814.htm#f&cst=null&cud=0&pg=1-26&prod=&sc=107294']
    #'https://www.alza.cz/herni-notebooky/18848814.htm#f&cst=null&cud=0&pg=1-26&prod=&sc=107294'

    def __init__(self):
        scrapy.Spider.__init__(self)
        # use any browser you wish
        self.browser = webdriver.Firefox()

    def __del__(self):
        self.browser.close()

    def start_request(self):
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        self.browser.get('https://www.alza.cz/herni-notebooky/18848814.htm#f&cst=null&cud=0&pg=1-26&prod=&sc=107294')
        time.sleep(3)
        hxs = scrapy.Selector(text=self.browser.page_source)
        notebooks = hxs.css('div.fb')
        for notebook in notebooks:
            links_to_follow = "https://www.alza.cz" + notebook.xpath('./a/@href').extract_first() + "#parametry"
            yield response.follow(url=links_to_follow, callback=self.parse_notebooks)

    def parse_notebooks(self, response):
        top_table = response.xpath('//div[contains(@class, "groupValues js-top-parameters")]/div[contains(@class, "row")]/span[@class="value"]/text()')
        table_disp = response.xpath('//div[@class="allpar"]//div[contains(@class, "row")]/span[@class="value"]/text()')
        name = response.xpath('//a[contains(@class, "last")]/text()').extract_first()
        notebooks_ram = top_table.extract()[1]
        notebooks_cpu = top_table.extract()[2]
        notebooks_storage = top_table.extract()[0]
        notebooks_resolution = table_disp.extract()[1]
        notebooks_ref_rate = table_disp.extract()[3]
        notebooks_gpu = table_disp.extract()[24]
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