import os
import jinja2
import webapp2

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

app =   webapp2.WSGIApplication([
    ('/', HomePage),
    ('/aboutus', AboutPage)
], debug=True)
