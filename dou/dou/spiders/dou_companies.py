# -*- coding: utf-8 -*-
import scrapy


class DouCompaniesSpider(scrapy.Spider):
    name = 'dou_companies'
    allowed_domains = ['https://jobs.dou.ua/companies/']
    start_urls = ['https://jobs.dou.ua/companies/']
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def parse(self, response):
        for company in response.xpath(".//*[@id='companiesListId']/ul/li[@class='l-company']/div[@class='company']"):
            print(company)
            yield {

                'company_name': company.xpath("div[@class='ovh']/div[1]/a/text()").extract_first(),
                'company_profile': company.xpath("div[@class='ovh']/div[1]/a/@href").extract_first(),
                'description': company.xpath("div[@class='ovh']/div[@class='descr']/text()").extract_first(),
                
                
            }
