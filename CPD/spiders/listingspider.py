import scrapy


class ListingspiderSpider(scrapy.Spider):
    name = 'listingspider'
    allowed_domains = ['api.coinmarketcap.com']
    start_urls = ['http://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing']
    
    def parse(self, response):
        listing = response.json()["data"]["cryptoCurrencyList"]
        for crypto in listing:
            yield{
                "id": crypto["id"],
                "name": crypto["name"],
                "symbol": crypto["symbol"],
            }
