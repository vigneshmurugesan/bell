import tornado.web

class CrawlHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Should I crawl now?\n')

