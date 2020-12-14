import scrapy
from moreinfo_crawler.items import DoubanBook250Item

class DoubanBook250Spider(scrapy.Spider):
    name = 'douban_book_250'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']


    def parse(self, response):

        find_all = response.xpath('//div[@class="article"]/div[@class="indent"]/table/tr[@class="item"]')
        for section in find_all:
            try:
                # release_time = section.xpath("td[2]/p[@class='pl']/text()").extract()[0].strip().split('/')[-2]
                # price = section.xpath("td[2]/p[@class='pl']/text()").extract()[0].strip().split('/')[-1]
                # item['release_time'] = release_time
                # item['price'] = price

                item = DoubanBook250Item()
                item['title'] = section.xpath("td[2]/div[@class='pl2']/a/text()").extract_first().strip()
                item['cover_url'] = section.xpath("td[1]/a/img/@src").extract_first().replace('\n', '').strip()
                item['url'] = section.xpath("td[1]/a/@href").extract_first().strip()
                item['author'] = section.xpath("td[2]/p[@class='pl']/text()").extract()[0].strip().split('/')[0]
                item['publisher'] = section.xpath("td[2]/p[@class='pl']/text()").extract()[0].strip().split('/')[-3]
                item['score'] = section.xpath("td[2]/div[@class='star clearfix']/span[@class='rating_nums']/text()").extract_first()
                item['score_num'] = section.xpath("td[2]/div[@class='star clearfix']/span[@class='pl']/text()").extract_first().strip('\n )(')
                item['simple_comment'] = section.xpath("td[2]/p[@class='quote']/span[@class='inq']/text()").extract_first()
                yield item
            except:
                print(f'{section} error')
                pass

        urls = ['https://book.douban.com/top250?start={0}'.format(i) for i in range(25, 275, 25)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

