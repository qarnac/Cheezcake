import os
import jinja2
import webapp2
from pytrends.request import TrendReq
from datetime import datetime

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        #
        # pytrends = TrendReq(hl='en-US', tz=360)
        # musictable = pytrends.top_charts(yyyymm, 'music', geo='us', cat='')

        mypage = env.get_template('templates/home.html')
        self.response.write(mypage.render())

app =   webapp2.WSGIApplication([
    ('/', HomePage),
], debug=True)
