# -*- coding:utf-8 -*-


import tornado.web

class DeleteHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument("id",None)
        cursor = self.application.cursor
        if id:
            insert_sql = "delete from blog where id={0}".format(id)
            cursor.execute(insert_sql)
            self.application.conn.commit()
            sql="alter table blog auto_increment={0}".format(id)
            cursor.execute(sql)
            self.application.conn.commit()

        self.redirect('/blog')

    def post(self):
        pass