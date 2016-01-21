import scrapy 
import re
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from imgur.items import ImgurItem

      
class ImgurSpider(CrawlSpider):
    name = 'cardekho'
    allowed_domains = ['cardekho.com']
    start_urls = ['http://www.cardekho.com/new-cars+5-lakh-10-lakh']
    # rules = [Rule(LinkExtractor(allow=['/events-listing/.*']), 'parse_imgur')]

    def parse(self,response):
        item = ImgurItem()
        for event in response.xpath("//div[contains(concat(' ', @class, ' '), ' listing ')]/ul/li"):
            # print event.xpath("./a/@href").extract()
            check_img = str(event.xpath("./div[1]/div[2]/div[1]/a/@href").extract())
            # print check_img
            for checks_image in check_img:
                item['title'] = event.xpath("./div[1]/div[2]/div[1]/a/text()").extract()
                item['mileage'] = event.xpath("./div[1]/div[2]/div[2]/ul/li[1]/text()").extract()
                item['engineDisplacement'] = event.xpath("./div[1]/div[2]/div[2]/ul/li[2]/text()").extract()
                item['seatingCapacity'] = event.xpath("./div[1]/div[2]/div[2]/ul/li[3]/text()").extract()
                price = event.xpath("./div[1]/div[3]/div[1]/text()").extract()
                pat = re.compile(r'(\d{1,2}\.\d{1,2}\-\s\d{1,2}\.\d{1,2}\w+)'%price)
                item['price'] = pat
                print pat
                item['image_urls'] = event.xpath("./div[1]/div[1]/a/img/@data-original").extract()
                yield item