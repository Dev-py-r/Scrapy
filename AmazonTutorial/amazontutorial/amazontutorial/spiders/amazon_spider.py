#scrapy startproject amazontutorial
#cd amazontutorial
#scrapy genspider amazon_spider amazon.com

import scrapy
from ..items import AmazontutorialItem
from scrapy.loader.processors import MapCompose

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    #scraping multiple page
    page_number = 2
    start_urls = [
        'https://www.amazon.com/gp/bestsellers/books/283155/ref=s9_acsd_ri_bw_clnk/ref=s9_acsd_ri_bw_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-10&pf_rd_r=MWR673QB5M2442BSW6HS&pf_rd_t=101&pf_rd_p=d2e01c79-7462-4300-8d41-3633536344dc&pf_rd_i=283155'
    ]

    def parse(self, response):
        items = AmazontutorialItem()


        # product_name = []
        # for a in response.css('div.p13n-sc-truncate').css('::text').extract():
        #     product_name.append(a.strip())
        # product_name = response.xpath('//div[has-class("p13n-sc-truncate")]/text()').extract()

        product_name = response.css('div.p13n-sc-truncate').css('::text').extract()
        product_author = response.css('.a-link-normal+ .a-size-small .a-size-small').css('::text').extract()
        product_price = response.css('.p13n-sc-price').css('::text').extract()
        product_imagelink = response.css('img::attr(src)').extract()

        for product_name, product_author,product_price,product_imagelink in zip(product_name, product_author,product_price,product_imagelink):
            yield {
                'price_name': product_name.strip(),
                'product_author': product_author,
                'product_price': product_price,
                'product_imagelink': product_imagelink
            }

        # items['product_name'] = product_name
        # items['product_author'] = product_author
        # items['product_price'] = product_price
        # items['product_imagelink'] = product_imagelink
        #
        # yield items



        #pip install scrapy-user-agents
        #Bypassing usering user agent
        #Bypassing using proxies
        # scrapy - proxy - pool
        # https://github.com/hyan15/scrapy-proxy-pool

        # next_page = 'https://www.amazon.com/Best-Sellers-Books/zgbs/books/283155/ref=zg_bs_pg_2?_encoding=UTF8&pg=+ str(AmazonSpiderSpider.page_number)+'
        # 'https: // www.amazon.com / Best - Sellers - Books / zgbs / books / 283155 / ref = zg_bs_pg_2?_encoding = UTF8 & pg = ' + str(AmazonSpiderSpider.page_number)
        #
        # if AmazonSpiderSpider.page_number <= 100:
        #     AmazonSpiderSpider.page_number += 1
        # yield response.follow(next_page, callback=self.parse)

        # Add google bot

