# -*- coding:utf-8 -*-


from handlers.MainHanlder import MainHandler
from handlers.ChatSocketHandler import ChatSocketHandler

url=[
    (r'/', MainHandler),
    (r'/index',ChatSocketHandler)
    ]