# coding = utf-8

from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute('scrapy crawl jianshu -s CLOSESPIDER_ITEMCOUNT=10'.split())
    # cmdline.execute('scrapy crawl douban_book_search -a keyword=java -a start=15'.split())
    cmdline.execute('scrapy crawl douban_book_250 -o douban_book_250.csv'.split())