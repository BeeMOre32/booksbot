import scrapy

class TrickcalSpider(scrapy.Spider):
    name = "trickcal"
    allowed_domains = ["trickcal.com"]
    start_urls = [
        'https://trickcal.com/',
    ]

    def parse(self, response):
        count = response.css("p.el.count::text").extract_first()
        yield {'count': count}
