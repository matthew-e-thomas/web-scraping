# Matt Thomas
#met8k
# Module 4 Homework: Python and Web Scraper
import scrapy


class TotalwinelistSpider(scrapy.Spider):
    name = 'totalwinelist'
    allowed_domains = ['https://www.totalwine.com']
    start_urls = ['https://www.totalwine.com/wine/red-wine/pinot-noir/c/000018?pagesize=180']#sets the website we start from

    custom_settings={ 'FEED_URI': "totalwinelist.csv",  #this uses scrapy's functions to save as csv file
                       'FEED_FORMAT': 'csv'}


    def parse(self, response): #extract data and store in variables using xpath
        product_name = response.xpath('//a[@class="analyticsProductName"]/text()').extract()
        price = response.xpath('//span[@class="price"]/text()').extract()
        desc = response.xpath('//span[@class="winespec-desc-txt"]/text()').extract()
      
        row_data = zip(product_name, price, desc)
        
        for item in row_data: #iterates through and creates a dictionary
            scraped_info = {
                    'Product':item[0],
                    'Price': item[1],
                    'Description':item[2]
                
            
                  
                    
                    }
            yield scraped_info
        
        #This is the section where I attempted to 'crawl' across the website to visit all
        #the wines, but it doesn't work because the href attricute is a javascript on totalwine's website
        next_page = response.css('.floatLeft a::attr(href)').extract_first()  
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            
         