import scrapy

class ImgurItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    mileage = scrapy.Field()
    engineDisplacement = scrapy.Field()
    seatingCapacity = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
