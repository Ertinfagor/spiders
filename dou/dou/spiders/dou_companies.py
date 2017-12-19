# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from scrapy.http import HtmlResponse


driver = webdriver.Chrome()

class DouCompaniesSpider(scrapy.Spider):
    name = 'dou_companies'
    allowed_domains = ['https://jobs.dou.ua/companies/']
    start_urls = ['https://jobs.dou.ua/companies//']

    driver.get("https://jobs.dou.ua/companies/")
    for x in range(0,2):
        elem = driver.find_element_by_xpath("""//*[@id="companiesListId"]/div/a""")
        elem.click()
        time.sleep(1)


    def parse(self, response):
        response = HtmlResponse(url="my HTML string", body=driver.page_source, encoding='utf-8')

        for company in response.xpath("//div[@class='company']"):
            yield {

                'company_name': company.xpath("div[@class='ovh']/div[1]/a/text()").extract_first(),
                'company_profile': company.xpath("div[@class='ovh']/div[1]/a/@href").extract_first(),
#                'description': company.xpath("div[@class='ovh']/div[@class='descr']/text()").extract_first(),
#                'city': company.xpath("//span[@class='city']/text()").extract_first(),


            }
