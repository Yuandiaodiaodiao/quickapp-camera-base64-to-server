import tornado.web
import base64
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        print(self.request.body)
        imageb64=self.request.body
        import base64
        image=base64.b64decode(imageb64)
        with open('image.jpg','wb') as f:
            f.write(image)
        self.write("ok")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
