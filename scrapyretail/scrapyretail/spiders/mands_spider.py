import scrapy
import openpyxl
from..items import mandsItem

mandsUrls = []
wb_obj = openpyxl.load_workbook('/Users/kathrynhewitt/PycharmProjects/ScrapyRetail/scrapyretail/scrapyretail/Inputs/msURLs.xlsx')
sheet_obj = wb_obj.active
for i in range (1, 71):
    cell_obj = sheet_obj.cell(row=i, column=1)
    textd = cell_obj.value
    mandsUrls.append(textd)
print(mandsUrls)


class mandsSpider(scrapy.Spider):
    name = 'MandS'
    start_urls = mandsUrls

    def parse(self, response):

        items = mandsItem()

        name = response.css("#overview > section.bop-section.bop-intro > header > h2::text")[0].extract()
        price = response.css(".bop-price__current::text").extract()
        amount = response.css(".bop-price__per::text")[0].extract()
        weight = response.css(".bop-catchWeight::text").extract()

        items['name'] = name
        items['price'] = price
        items['amount'] = amount
        items['weight'] = weight

        yield items
