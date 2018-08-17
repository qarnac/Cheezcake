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
        for p in q.fetch(10):
            string.append((str(p.ranking) + ": " + p.title + " by " + p.info))

        q2 = DataItem.query(DataItem.category == 'music-us')
        q2 = q2.order(DataItem.ranking)
        string2 = []
        for p in q2.fetch(10):
            string2.append((str(p.ranking) + ": " + p.title + " by " + p.info))

        q3 = DataItem.query(DataItem.category == 'music-artists')
        q3 = q3 .order(DataItem.ranking)
        string3 = []
        for p in q3.fetch(10):
            string3.append((str(p.ranking) + ": " + p.title))

        self.response.out.write(mypage.render({'elements1': string,
                                               'elements2': string2, 'elements3':string3}))

class MoviePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/movie.html')

        q = DataItem.query(DataItem.category == 'movies')
        q = q.order(DataItem.ranking)
        string = []

        for p in q.fetch(10):
            string.append((str(p.ranking) + ": " + p.title))

        q2 = DataItem.query(DataItem.category == 'movies-us')
        q2 = q2.order(DataItem.ranking)
        string2 = []
        for p in q2.fetch(10):
            string2.append((str(p.ranking) + ": " + p.title))

        q3 = DataItem.query(DataItem.category == 'upcoming')
        q3 = q3 .order(DataItem.ranking)
        string3 = []
        for p in q3.fetch(10):
            string3.append((str(p.ranking) + ": "+ p.title))

        self.response.out.write(mypage.render({'elements1': string,
                                               'elements2': string2, 'elements3':string3}))

class GamePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/game.html')

        q = DataItem.query(DataItem.category == 'top-games')
        q = q.order(DataItem.ranking)
        string = []
        for p in q.fetch(10):
            string.append((str(p.ranking) + ": " + p.title))

        q2 = DataItem.query(DataItem.category == 'trending-games')
        q2 = q2.order(DataItem.ranking)
        string2 = []
        for p in q2.fetch(10):
            string2.append((str(p.ranking) + ": " + p.title))

        q3 = DataItem.query(DataItem.category == 'top-board')
        q3 = q3 .order(DataItem.ranking)
        string3 = []
        for p in q3.fetch(10):
            string3.append((str(p.ranking) + ": " + p.title))

        self.response.out.write(mypage.render({'elements1': string,
                                               'elements2': string2, 'elements3':string3}))

class BookPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/book.html')

        q = DataItem.query(DataItem.category == 'top-books')
        q = q.order(DataItem.ranking)
        string = []
        for p in q.fetch(10):
            string.append((str(p.ranking) + ": " + p.title + " by " + p.info))

        q2 = DataItem.query(DataItem.category == 'top-us')
        q2 = q2.order(DataItem.ranking)
        string2 = []
        for p in q2.fetch(10):
            string2.append((str(p.ranking) + ": " + p.title + " by " + p.info))

        q3 = DataItem.query(DataItem.category == 'authors')
        q3 = q3 .order(DataItem.ranking)
        string3 = []
        for p in q3.fetch(10):
            string3.append((str(p.ranking) + ": " + p.title))

        self.response.out.write(mypage.render({'elements1': string,
                                               'elements2': string2, 'elements3':string3}))

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

        newItem = DataItem(category=cat, ranking=ranking, title=title,
                           info=info, imgsrc=imgsrc)
        newItem.put()

        mypage = env.get_template('templates/datadev.html')
        self.response.write(mypage.render())

app =   webapp2.WSGIApplication([
    ('/', HomePage),
    ('/home', HomePage),
    ('/aboutus', AboutPage),
    ('/music', MusicPage),
    ('/movie', MoviePage),
    ('/game', GamePage),
    ('/book', BookPage),
    ('/datadev', dataDev)
], debug=True)
