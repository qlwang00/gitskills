# -*- coding:utf-8 -*-

import tornado.web
from handlers.ChatSocketHandler import ChatSocketHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.render("index.html", messages=ChatSocketHandler.cache)
        self.render("index.html")
