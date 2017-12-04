# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from Zufang.settings import USER_AGENTS
import random, requests, json


class ZufangSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AnjukeUseragentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENTS)
        # print(ua)
        request.headers['User-Agent'] = ua


class AnjukeProxyMiddleware(object):
    def __init__(self):
        self.proxy = requests.get("http://127.0.0.1:5010/get/").text
        print(self.proxy)
        self.check_ip()

    def process_request(self, request, spider):
        print(self.proxy)
        request.meta['proxy'] = 'http://' + self.proxy

    def process_response(self, request, response, spider):
        print('++++++++++++++++++++')
        if response.status != '200':
            print(11111111111)
            self.proxy = requests.get("http://127.0.0.1:5010/get/").text
            self.check_ip()
            return request

    def check_ip(self):
        while True:
            try:
                response = requests.get('http://httpbin.org/ip', proxies={"http": "http://{}".format(self.proxy)}, timeout=3)
                # 使用代理访问
                print(response.text)
                if 'origin' not in json.loads(response.text):
                    print('error-1')
                    self.proxy = requests.get("http://127.0.0.1:5010/get/").text
                    print(self.proxy)
                else:
                    break
            except Exception:
                print('error-2')
                self.proxy = requests.get("http://127.0.0.1:5010/get/").text
                print(self.proxy)