# -*- coding:utf-8 -*-



import tornado.web

class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        cursor=self.application.cursor
        cursor.execute('select * from blog order by date')
        res=cursor.fetchall()

        if len(res):
            self.render("blog.html",
                        page_title=res[0][0],
                        # title=res[0][0],
                        # content=res[0][1],
                        # date=res[0][2]
                        res=res
                        )
        else:
            self.redirect('/')
