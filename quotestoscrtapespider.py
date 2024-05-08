import scrapy


base_url = "https://quotes.toscrape.com/api/quotes?page={}"

class QuotestoscrtapespiderSpider(scrapy.Spider):
    name = "quotestoscrtapespider"
    # allowed_domains = ["x"]
    start_urls = [base_url.format(1)]

    def parse(self, response):
        data = response.json() # scrapy version 2.2
        # print(data['has_next'])
        # print(data['page'])
        
        for quote in data["quotes"]:
            
            yield {
                "author": quote["author"]['name'],
                "Quote": quote['text']
            }
        current_page = data["page"]
        
        if data['has_next']:
            
            next_page_url = base_url.format(current_page+1)
            yield scrapy.Request(next_page_url)
            
            

