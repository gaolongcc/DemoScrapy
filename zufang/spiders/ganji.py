#-*-coding: utf-8 -*-
import scrapy
from ..items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ['https://su.fang.anjuke.com/loupan/?from=navigation/']


    def parse(self, response):
        print(response)
        #sel = Selector()
        zf = ZufangItem()
        info_list = response.xpath('//div[@class="key-list"]/div')
        #money_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        #title_list = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        for ench in info_list:
            money = ench.xpath("./a[2]/p[1]/span/text()").extract()
            title = ench.xpath("./div/a[1]/h3/span/text()").extract()

            if len(money):
                zf['title'] = title[0]
                zf['money'] = money[0]
                yield zf

        #for i, j in zip(title_list, money_list):
        #   zf['title'] = i.encode('utf-8')
        #    zf['money'] = j.encode('utf-8')
        #    yield zf
        #for i in range(len(money_list)):
        #  if i < len(title_list):
        #       #zf['title'] = title_list[i]
        #       #zf['money'] = money_list[i]
        #      yield {
                   # return some results
        #            'title': title_list[i],
        #            'money': money_list[i],
        #        }
        #      yield zf