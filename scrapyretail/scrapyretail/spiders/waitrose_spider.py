import scrapy
import openpyxl
from..items import waitroseItem

waitroseUrls = []
wb_obj = openpyxl.load_workbook('/Users/kathrynhewitt/PycharmProjects/ScrapyRetail/scrapyretail/scrapyretail/Inputs/waitroseURLs.xlsx')
sheet_obj = wb_obj.active
for i in range (1, 68):
    cell_obj = sheet_obj.cell(row=i, column=1)
    textd = cell_obj.value
    waitroseUrls.append(textd)
print(waitroseUrls)


class waitroseSpider(scrapy.Spider):
    name = 'waitrose'
    start_urls = waitroseUrls

    def parse(self, response):

        items = waitroseItem()

        name = response.css(".name___30fwb::text").extract()
        price = response.css(".productPricing___1GkLr span span::text")[1].extract()
        amount = response.css(".pricePerUnit___1L8TG::text").extract()
        weight = response.css(".sizeMessage___3o5Ri::text").extract()

        items['name'] = name
        items['price'] = price
        items['amount'] = amount
        items['weight'] = weight

        yield items





