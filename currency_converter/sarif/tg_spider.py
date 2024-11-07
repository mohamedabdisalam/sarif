import scrapy

class TransferGalaxySpider(scrapy.Spider):
    name = 'transfergalaxy'
    start_urls = ['https://transfergalaxy.com/en/destination/somalia/']

    def parse(self, response):
        data = {}
        calculation_div = response.xpath('//div[@class="calculation"]')
        #Extracting you send amount
        data['you_send'] = calculation_div.xpath(".//th[text()='You send']/following-sibling::td/text()").get()
        data['exchange_rate'] = calculation_div.xpath(
            ".//table[@class='index-table']//th[text()='Exchange rate']/following-sibling::td/text()").get()
        yield data