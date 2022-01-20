# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Top250ShowsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    show_name = scrapy.Field()
    release_date = scrapy.Field()
    imdb_rating = scrapy.Field()
    image_link = scrapy.Field()
    
    pass
