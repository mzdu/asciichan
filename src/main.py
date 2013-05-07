import os
import webapp2
import jinja2

from google.appengine.ext import db

#jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
                               autoescape = True)

def process(str1):
    # use TF-IDF to process str1 and extract keywords from article
    pass
    







class Art(db.Model):
    #indicate title is String type
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    #set it to current time
    created = db.DateTimeProperty(auto_now_add = True)
    
    keywords = db.StringListProperty()


class Handler(webapp2.RequestHandler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("select * from Art order by created DESC")
        
        self.render("index.html", title1=title, art1=art, error1=error, arts1=arts)
        
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
class MainPage(Handler):
    def get(self):
        self.render_front()
        
    def post(self):
        title2 = self.request.get("title1")
        art2 = self.request.get("art1")
        keywords = process(art2)
        
        if title2 and art2:
            a = Art(title=title2,art=art2, keywords=keywords)
            #add data to database
            a.put()
            self.redirect('/')
        else:
            error2 = "Sorry Error."
            
            self.render_front(title2, art2, error2)
    
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)