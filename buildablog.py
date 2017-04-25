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


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
 # Using templates instead of doing string substitutions for big html sections.
 # HTML is keept in separate files. These files have escapes for variables.


class Handler(webapp2.RequestHandler):
    """ Has one function (write). This is parent class. Base RequestHandler class
    for app. Other handlers inherit from this. """
    def write(self, *a, **kw):
        self.response.write(*a, **kw)
        # The above allows the function call to be abbreviated to self.write

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class Blogpost(db.Model):
    """ Represents blogpost to be written or written. Database """
    # This creates the database columns for tables.
    title = db.StringProperty(required = True)
    blogpost = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class MainHandler(Handler):
    """ Handles requests coming in to '/' root of Build a Blog site. """

    def render_form(self, title="", blogpost="", error=""):
        blogposts = db.GqlQuery("SELECT * FROM Blogpost ORDER BY created DESC")

        self.render("newpost.html", title=title, blogpost=blogpost, error=error,
                    blogposts = blogposts)

    def get(self):
        self.redirect("/mainblog")
        # Landing page appears.


class MainBlog(Handler):
    """ handles requests coming in to '/mainblog' """
    def get(self):
        """ Show a list of the blogs that user has already written """
        query = Blogpost.all().order("created")
        # get the first 5 results
        written_posts = query.fetch(limit = 5)

        # t = jinja_env.get_template("mainblog.html")
        self.render("mainblog.html", blogposts = written_posts)
        # self.response.write(content)


class Newpost(Handler):
    """ handles requests coming in to '/newpost' """
    """user wants to enter title and blog copy."""
    def get(self):
        self.render("newpost.html")

    def post(self):
        """ Write a title and blog text. """
        written_title = self.request.get("title")
        written_blogpost = self.request.get("blogpost")

        if written_title and written_blogpost:
            b = Blogpost(title = written_title, blogpost = written_blogpost)
            # Making new instance. Input goes into database
            b.put()

            self.redirect('/')
        else:
            error = "Both title and blogpost are required!"

            self.render("newpost.html", new_title = written_title,
                        new_blogpost = written_blogpost, error=error)


class DisplayPost(Handler):
    def get(self, id):
        key = db.Key.from_path("Blogpost", int(id))
        blogpost = db.get(key)

        if not blogpost:
            self.error(404)
            return

        self.render("permalink.html", blogpost=blogpost)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newpost', Newpost),
    ('/mainblog', MainBlog),
    webapp2.Route('/displaypost/<id:\d+>', DisplayPost)],
    debug=True)
