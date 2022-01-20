import scrapy
from ..items import AmazonbooksItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ["https://www.amazon.in/s?i=stripbooks&bbn=976390031&rh=n%3A976389031%2Cn%3A1318105031%2Cp_n_publication_date%3A2684819031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_72%3A1318476031&dc&qid=1641237557&rnid=976390031&ref=sr_nr_n_7"]

    def parse(self, response):
        items = AmazonbooksItem()
        book_name = response.css('.a-color-base.a-text-normal::text').extract()
        book_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        book_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extrat()
        book_imagelink = response.css('.s-image-fixed-height::attr(src)').extarct()

        items['book name'] = book_name
        items['book author'] = book_author
        items['book price'] = book_price
        items['book image'] = book_imagelink

        yield items
