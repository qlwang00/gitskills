# -*- coding:utf-8 -*-


from handlers.MainHandler import MainHandler
from handlers.BlogHandler import BlogHandler
from handlers.EditHandle import EditHandler
from handlers.DeleteHandler import DeleteHandler

url=[
    (r"/", MainHandler),
    (r"/blog", BlogHandler),
    (r"/query",EditHandler),
    (r"/delete", DeleteHandler),
    ]