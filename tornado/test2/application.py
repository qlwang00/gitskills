# -*- coding:utf-8 -*-


import tornado
import os
from url import url

import mysql.connector

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )

        self.conn=mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            db='test'
        )
        self.cursor=self.conn.cursor()

        tornado.web.Application.__init__(self,url, **settings)