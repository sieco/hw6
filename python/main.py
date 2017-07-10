#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(u"""
            <html>
             <head>
              <title>パタトクカシーー</title>
             </head>
             <body>
             <center>
            　<font size="10">
              <hl><b><big>こんにちは！</big></b></hl>
		 <hr width = "300">
              <form action="/sub" method="post">
                <input type = "text" name="text1"><br>
                <input type = "text" name="text2"><br>
                <input type = "submit" name = "submit">
              </form>
              </font>
             </center>
             </body>
             </html>
            """)

class SubPage(webapp2.RequestHandler):
    def post(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        text1 = self.request.get("text1")
        text2 = self.request.get("text2")
        sub = "".join(i+j for i, j in zip(text1,text2))
        self.response.out.write(u"""
              <html>
              <head>
              <title>パタトクカシーー</title>
             </head>
        """)
        if(sub != ""):
            self.response.out.write(u"""
               <body>
               <center>
            　<font size="10">%s</font>
		 <hr width = "300">
               </center>
                </body>
             """%sub)
        self.response.out.write(u"""
             <body>
              <center>
              <form action="/sub" method="post">
                <input type = "text" name="text1"><br>
                <input type = "text" name="text2"><br>
                <input type = "submit" name = "submit">
              </form>
              </center>
              </body>
             </html>
            """)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ("/sub", SubPage)
], debug=True)
