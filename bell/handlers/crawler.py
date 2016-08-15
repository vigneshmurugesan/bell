import tornado.web

from controller import crawl

class CrawlHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Should I crawl now?\n')
        crawler = crawl.Crawler()

        # TODO: Define a handler and handle this internally
        crawler.get_symbol_data('AAPL')
