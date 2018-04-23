# -*- coding:utf-8 -*-


import tornado.web

class EditHandler(tornado.web.RequestHandler):
    def get(self):
        id=self.get_argument("id",None)
        cursor = self.application.cursor
        if id:
            select_sql = "select * from blog where id={0}".format(id)
            cursor.execute(select_sql)
            res=cursor.fetchall()
            self.render(
                "query.html",
                page_title=res[0][0],
                res=res
            )

    def post(self):
        import time
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        if title and content:
            date = int(time.time())
            cursor = self.application.cursor
            update_sql = "update blog set title={0},content={1},date={2}".format(title, content, date)
            cursor.execute(update_sql)
            self.application.conn.commit()

        self.redirect('/blog')