import tornado.web
import tornado.httpserver
import tornado.ioloop
import logging
import time
from handlers import dd as dd_handlers

HANDLERS = [
    # 登录
    (r"/api/getUserInfo", dd_handlers.UserHandler),
    # 钉钉组织架构同步
]
logging.basicConfig(filename=f"./log/web.{time.strftime('%Y_%m_%d')}.txt",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def run():
    app = tornado.web.Application(
        HANDLERS
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8091
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
