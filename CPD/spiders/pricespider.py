import scrapy
import time


class PricespiderSpider(scrapy.Spider):
    name = 'pricespider'
    allowed_domains = ['web-api.coinmarketcap.com']
    
    def start_requests(self):
        yield scrapy.Request(f'https://web-api.coinmarketcap.com/v2/cryptocurrency/ohlcv/historical?id={self.cid}&convert=EUR&time_start=2013-04-28&time_end={self.date}')
    
    def parse(self, response):
        price = response.json()["data"]["quotes"]
        for crypto in price:
            yield{
                "time": crypto["time_close"][:10],
                "price": crypto["quote"]["EUR"]["close"],
            }
