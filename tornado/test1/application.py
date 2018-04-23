# -*- coding:utf-8 -*-

import tornado
from url import url
import os
# from handlers import MainHanlder,ChatSocketHandler

class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, url, **settings)