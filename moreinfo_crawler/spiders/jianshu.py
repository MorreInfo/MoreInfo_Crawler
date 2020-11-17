import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from moreinfo_crawler.items import JianShuArticleItem


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        # 观察url发现，前缀都一样，后面是12个数字加小写字母的组合
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        origin_url = response.url
        article_id = response.url.split("?")[0].split("/")[-1]
        title = response.xpath("//h1[@class='_1RuRku']/text()").extract_first('')
        avatar = response.xpath("//meta[@property='og:image']/@content").extract_first('')
        author = response.xpath("//span[@class='_22gUMi']/text()").extract_first()
        content = response.xpath("//article[@class='_2rhmJa']").get()
        description = response.xpath("//meta[@property='og:description']/@content").extract_first('')
        yield JianShuArticleItem(
            article_id=article_id,
            title=title,
            author=author,
            avatar=avatar,
            content=content,
            description=description,
            origin_url=origin_url)

