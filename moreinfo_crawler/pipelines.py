import json
import redis as redis

JIANSHU_ARTICLE_KEY = 'JIANSHU_ARTICLE'

class RedisPipeline:
    def open_spider(self, spider):
        # 第一个参数是settings.py里的属性，第二个参数是获取不到值的时候的替代值
        host = spider.settings.get("REDIS_HOST", "localhost")
        port = spider.settings.get("REDIS_PORT", 6379)
        db_index = spider.settings.get("REDIS_DB_INDEX", 0)
        db_psd = spider.settings.get("REDIS_PASSWORD", "")
        # 连接数据库
        self.db_conn = redis.StrictRedis(host=host, port=port, db=db_index, password=db_psd)

    def process_item(self, item, spider):
        # 将item转换成字典
        item_json = json.dumps(dict(item))
        # 将数据插入到集合
        self.db_conn.rpush(JIANSHU_ARTICLE_KEY, item_json)
        return item

    def close_spider(self, spider):
        # 关闭连接
        self.db_conn.connection_pool.disconnect()
