import scrapy
from ..items import Top250ShowsItem

class ImdbfinderSpider(scrapy.Spider):
    name = 'imdbfinder'
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    def parse(self, response):
        items = Top250ShowsItem()

        show_name = response.css('.titleColumn a::text').extract()
        release_date = response.css('.secondaryInfo::text').extract()
        imdb_rating = response.css('strong::text').extract()
        image_link = response.css('img::attr(src)').extract()
        """
        show_name = response.css('a').css('::text').extract()
        release_date = response.css('.secondaryInfo').css('::text').extract()
        imdb_rating = response.css('strong').css('::text').extract()
        image_link = response.css('img::attr(src)').extract()
        """
        items['show_name'] = show_name
        items['release_date'] = release_date
        items['imdb_rating'] = imdb_rating
        items['image_link'] = image_link

        yield items