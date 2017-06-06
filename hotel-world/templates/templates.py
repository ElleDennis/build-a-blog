import webapp2

import jinja2
import os

# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
# Above "templates" represents the name of the file in which jinja is set.
# Python syntax below for multi-line string
# percent s is Python string formatting character


class Handler(webapp2.RequestHandler):
    # Has one function (write). This is parent class.
    def write(self, *a, **kw):
        self.response.write(*a, **kw)
        # The above allows the function call to be abbreviated to self.write

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
        # Function takes a file name (template) and extra parameters
        # (Python syntax)
        # Jinja environment, get_template and give it file name. Loads file and
        # create template and store it in t.

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    # MainHandler (this is the main page) inherits from class called Handler
    # Handler is defined in the preceding class.
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items = items)
        # Above gets 'food', stores in items.
        # self.render passes items into template. Here variable name is same
        # as content.


class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
