# -*- coding:utf-8 -*-

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        import time
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        if title and content:
            date=int(time.time())
            cursor=self.application.cursor
            insert_sql="insert into blog(title,content,date) values('{0}','{1}',{2})".format(title,content,date)
            cursor.execute(insert_sql)
            self.application.conn.commit()

        self.redirect('/blog')