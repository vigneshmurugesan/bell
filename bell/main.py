import tornado.ioloop
import tornado.web

from handlers import default, crawler

APP_HANDLERS = [
    (r"/",          default.MainHandler),
    (r"/crawl",     crawler.CrawlHandler),
]

def make_app():
    return tornado.web.Application(APP_HANDLERS)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
