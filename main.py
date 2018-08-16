import os
import jinja2
import webapp2
from models import DataItem
import logging


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/home.html')
        self.response.write(mypage.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/about.html')
        self.response.write(mypage.render())

class MusicPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/music.html')
        q = DataItem.query(DataItem.category == 'music')
        q = q.order(DataItem.ranking)

        string = []
        for p in q.fetch():
            string.append((str(p.ranking) + ": " + p.title + " by " + p.info))

        self.response.out.write(mypage.render({'elements1': string}))

class MoviePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/movie.html')
        self.response.write(mypage.render())

class GamePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/game.html')
        self.response.write(mypage.render())

class BookPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/book.html')
        self.response.write(mypage.render())

class dataDev(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/datadev.html')
        self.response.write(mypage.render())

    def post(self):
        cat = self.request.get('category')
        ranking = int(self.request.get('ranking'))
        title = self.request.get('title')
        info = self.request.get('info')
        imgsrc = self.request.get('imgsrc')

        newItem = DataItem(category=cat, ranking=ranking, title=title, info=info, imgsrc=imgsrc)
        newItem.put()

        mypage = env.get_template('templates/datadev.html')
        self.response.write(mypage.render())

app =   webapp2.WSGIApplication([
    ('/', HomePage),
    ('/aboutus', AboutPage),
    ('/music', MusicPage),
    ('/movie', MoviePage),
    ('/game', GamePage),
    ('/book', BookPage),
    ('/datadev', dataDev)
], debug=True)
