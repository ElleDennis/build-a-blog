#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2

from google.appengine.ext import db


# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
# Above "templates" represents the name of the file in which jinja is set.
# Python syntax below for multi-line string
# percent s is Python string formatting character. Jinja renders html.


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


class Art(db.Model):
    # This creates the database columns for tables.
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class MainHandler(Handler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art "
                           "ORDER BY created DESC")

        self.render("front.html", title=title, art=art, error=error, arts = arts)
        # Above passes variables into form template.

    def get(self):
        self.render_front()
        # Draws blank form.

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            # Making new instance.
            a.put()

            self.redirect('/')
        else:
            error = "We need both title and artwork!"
            self.render_front(title, art, error)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
