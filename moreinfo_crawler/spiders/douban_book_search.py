import scrapy
import execjs
import re
import pathlib

from moreinfo_crawler.items import DouBanBookSearchItem


class DoubanBookSearchSpider(scrapy.Spider):
    name = 'douban_book_search'
    allowed_domains = ['douban.com']

    def __init__(self,keyword=None,start=None,*args, **kwargs):
        super(DoubanBookSearchSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.start = start
        self.start_urls.append(f'https://search.douban.com/book/subject_search?search_text={self.keyword}&cat=1001&start={self.start}')

    # @property
    # def keyword(self):
    #     return self.keyword

    def parse(self, response):
        r = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)
        # 导入js
        file_path = pathlib.Path.cwd() / 'third_party/main.js'
        with open(file_path, 'r', encoding='gbk') as f:
            decrypt_js = f.read()
        ctx = execjs.compile(decrypt_js)
        data = ctx.call('decrypt', r)
        for item in data['payload']['items']:
            if item.get('rating', None):
                cover_url = item['cover_url']
                score = item['rating']['value']
                score_num = item['rating']['count']
                url = item['url']
                abstract = item['abstract']
                title = item['title']
                id = item['id']
                yield DouBanBookSearchItem(
                    cover_url=cover_url,
                    score=score,
                    score_num=score_num,
                    url=url,
                    abstract=abstract,
                    title=title,
                    id=id)




