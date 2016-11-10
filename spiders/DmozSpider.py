import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DmozSpider(scrapy.Spider):

    name = 'dmoz'

    def __init__(self, *args, **kwargs):
      super(DmozSpider, self).__init__(*args, **kwargs)
      self.start_urls = [kwargs.get('start_url')]

    allowed_domains = ['dmoz.org']
    start_urls = []

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
