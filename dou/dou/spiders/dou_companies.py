# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class DouCompaniesSpider(scrapy.Spider):
    name = 'dou_companies'
    allowed_domains = ['https://jobs.dou.ua/companies/']
    start_urls = ['https://jobs.dou.ua/companies/']
    script = """
    function main(splash)
        assert(splash:go(splash.args.url))
        splash.resource_timeout = 3600
        splash:wait(5)  
        for i = 21,1,-1 
        do 
            splash:select(".more-btn>a").mouse_click()
            splash:wait(1)  
        end
        splash:wait(0.5)
        return  splash:html()
    end
    """    
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    def start_requests(self):

        
        yield SplashRequest(self.start_urls[0], self.parse, endpoint='execute', args={'lua_source': self.script, 'html': 1,})
    
    def parse(self, response):
        
        for company in response.xpath("//div[@class='company']"):
            yield {

                'company_name': company.xpath("div[@class='ovh']/div[1]/a/text()").extract_first(),
                'company_profile': company.xpath("div[@class='ovh']/div[1]/a/@href").extract_first(),
                'description': company.xpath("div[@class='ovh']/div[@class='descr']/text()").extract_first(),
                
                
            }
