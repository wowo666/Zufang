# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Zufang.items import ZufangItem

class AnjukeSpider(CrawlSpider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://xm.zu.anjuke.com/']

    rules = (
        # 翻页
        Rule(LinkExtractor(allow=r'/fangyuan/p\d+/$'), follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'/fangyuan/\d+$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print(response.url)
        item = ZufangItem()
        item['house_title'] = response.xpath('//*[@id="content"]/div[2]/div[1]/h3/text()').extract_first()
        item['link'] = response.url
        item['price'] = response.xpath('//dd[@class="og"]/strong/span/text()').extract_first()
        item['lease'] = response.xpath('//div[@class="box"]/div[1]/div[1]/dl[4]/dd/text()').extract_first()
        item['type'] = response.xpath('//div[@class="box"]/div[1]/div[1]/dl[3]/dd/text()').extract_first()
        item['estate'] = response.xpath('//div[@class="box"]/div[1]/div[1]/dl[5]/dd/a/text()').extract_first()
        item['floor'] = response.xpath('//div[@class="box"]/div[1]/div[2]/dl[5]/dd/text()').extract_first()
        item['addr'] = ''.join( response.xpath('//div[@class="box"]/div[1]/div[1]/dl[6]/dd/a/text()').extract())
        item['tel'] = response.xpath('//p[@class="broker-mobile"]/text()').extract_first()
        item['decoration'] = response.xpath('//div[@class="box"]/div[1]/div[2]/dl[2]/dd/text()').extract_first()
        item['area'] = response.xpath('//div[@class="box"]/div[1]/div[2]/dl[3]/dd/text()').extract_first()
        item['configuration'] = ' '.join( response.xpath('//*[@id="proLinks"]/p/span/text()').extract())
        item['desc'] = ' '.join( response.xpath('//*[@id="propContent"]/div/b/text()|//*[@id="propContent"]/div/p/text()|//*[@id="propContent"]/div/p/span/text()').extract()).replace('\t','').replace('\xb2','').replace('\xa0','')
        item['number'] = response.xpath('//div[@class="text-mute extra-info"]/text()').extract_first().split('：')[1].split('，')[0]
        item['pubdate'] = response.xpath('//div[@class="text-mute extra-info"]/text()').extract_first().split('：')[-1]
        yield item

