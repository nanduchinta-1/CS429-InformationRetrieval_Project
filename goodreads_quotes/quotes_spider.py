import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = [
        'https://www.goodreads.com/quotes',
    ]
    # Setting maximum page count
    max_pages = 100
    current_page_count = 0

    # Setting maximum depth
    DEPTH_LIMIT = 2
    
    #custom settings
    custom_settings = {
        'FEEDS': 
            {'quotes.json':{'format':'json', 'overwrite':True}
        }
    }
    def parse(self, response):
        # Increment page count
        self.current_page_count += 1
        quotes = response.css('div.quote')
        # Extract quotes and authors
        for q in quotes:
            yield {
                'text': q.css('div.quoteText::text').get().replace('”','').replace('“','').strip(),
                'author': q.css('span.authorOrTitle::text').get().strip(),
            }
        # Extract next page URL
        next_page = response.css('a.next_page::attr(href)').get()
         # Check if max page count is reached or next page exists
        if self.current_page_count < self.max_pages and next_page is not None:
            next_page_url = 'https://www.goodreads.com' + next_page
            yield response.follow(next_page_url, callback = self.parse)
        else:
            self.log(f"Reached max pages limit: {self.max_pages}")


        # Save quotes and authors to a txt file
        filename = f'quotes_page_{self.current_page_count}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for quote in response.css('div.quote'):
                text = quote.css('div.quoteText::text').get().replace('”','').replace('“','').strip()
                author = quote.css('span.authorOrTitle::text').get().strip()
                f.write(f'{text}-{author}\n')
'''
        # Check depth and follow links recursively
        if response.meta.get('depth', 1) < self.max_depth:
            for href in response.css('a::attr(href)').getall():
                yield response.follow(href, self.parse, meta={'depth': response.meta.get('depth', 0) + 1})
'''