# import scrapy
# from ..items import QuotetutorialItem
#
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'https://quotes.toscrape.com/'
#     ]


    #def parse(self, response):
        #title = response.css('title::text').extract()
        #yield {'titletext': title }


#scrapy shell "url"
#response.css("title")
#response.css("title").extract()
#response.css("title::text").extract()
#response.css("title::text")[0].extract() OR #response.css("title::text").extract_first()
#response.css("span.text::text").extract()
#response.css("span.text::text")[1].extract()

#Selector google chrome

#response.css(".author::text")[1].extract()

#terminal

#scrapy shell

#response.xpath().extract()

#response.xpath("//title/text()").extract()
#response.xpath("//span[@class='text']/text()")[1].extract()
#response.css("li.next a").xpath("@href").extract()
#response.css("a").xpath("@href").extract()

   #def parse(self,response):
        #all_div_quotes = response.css('div.quote')
        #title = all_div_quotes.css('span.text::text').extract()
        #author = all_div_quotes.css('.author::text').extract()
        #tag = all_div_quotes.css('.tag::text').extract()
        #yield {
    #   'title' : title,
    #      'author' : author,
    #       'tag' : tag
    #   }
    #   '''

    #def parse(self, response):
        #all_div_quotes = response.css('div.quote')


        #for quote in all_div_quotes:
            #title = quote.css('span.text::text').extract()
            #author = quote.css('.author::text').extract()
            #tag = quote.css('.tag::text').extract()
            #yield {
                #'title': title,
                #'author': author,
                #'tag': tag }


#https://doc.scrapy.org/en/latest/topics/items.html
#Extracted data -> Temporary containers (items) -> Storing in database

# Storing in container

    # def parse(self, response):
    #     items = QuotetutorialItem()
    #
    #     all_div_quotes = response.css('div.quote')
    #
    #     for quote in all_div_quotes:
    #         title = quote.css('span.text::text').extract()
    #         author = quote.css('.author::text').extract()
    #         tag = quote.css('.tag::text').extract()
    #
    #         items['title'] = title
    #         items['author'] = author
    #         items['tag'] = tag
    #
    #         yield items

        # Store in database
        # scrapy crawl quotes -o items.xml
        # scrapy crawl quotes -o items.json
        # scrapy crawl quotes -o items.csv

        # Scraped data -> Item containers -> Json/csv files
        # Scraped data -> Item containers -> Pipeline -> SQL/Mongo database

#Scrap from different pages

        # next_page = response.css('li.next a::attr(href)').get()
        # print(next_page)
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)