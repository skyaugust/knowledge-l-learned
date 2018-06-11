import tornado.ioloop
import tornado.web
import logging.config
import yaml

class MainHandler(tornado.web.RequestHandler):
    # 处理 HTTP 的 get put请求,。
    # 同步处理。当有很多请求来的时候，要等get方法结束。
    def get(self):
        self.write("Hello, world")
class MyFormHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.write('<html><body><form action="/submit" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))

class VideoHandler(tornado.web.RequestHandler):
    
    def get(self):
        
        self.write(u'{"id":"123","name":"甄嬛传"}')

def make_app():
    # Application 对象负责全局配置，包括路由表和请求-处理之间的映射
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/submit", MyFormHandler),
        (r"/qq", tornado.web.RedirectHandler, dict(url="http://www.qq.com")),
        (r"/video/example",VideoHandler)
    ])
    

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    import os
    print(os.listdir('./'))
    log_config = yaml.load(open('./python-tornado/logging.yaml', 'r'))
    logging.config.dictConfig(log_config)
    tornado.ioloop.IOLoop.current().start()