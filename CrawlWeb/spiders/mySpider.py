from scrapy.spiders import  Spider
from CrawlWeb.items import CrawlwebItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
class mySpider(Spider):
    name = "mySpider"
    start_urls=["https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.131.kExQPc&category=50025969&city=%B1%B1%BE%A9&province="]
    #https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.131.kExQPc&category=50025969&city=%B1%B1%BE%A9&province=

    def parse(self,response):
        filename="http"
        
        #print response.body
        print  "***"*10
        print response.url
        #print filename
        open(filename,'w').write(response.body)
        response=Selector(response)
        
        #unit=Selector(response).xpath('//li[@class="pai-item pai-status-doing"]')
        #unit=response.xpath('/html/body/div[3]/div[3]/div[3]/ul/li')
        #unit=response.xpath('//a[@class="linkwrap"]')
        #//*[@id="pai-item-538334015083"]
        unit=response.xpath(' //ul/li')
        #unit=response.xpath('//ul[@class="sf-pai-item-list"]')
        print  "***"*10 + "unit"
        print unit
        for mess in unit:
            item=CrawlwebItem()
            item['title']=mess.xpath('./a/div/p/text()').extract()
            print  "***"*10
            print item['title']


