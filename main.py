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
import webapp2
import random
import jinja2
import os
import logging
import json
from google.appengine.api import urlfetch
from pprint import pprint
import urllib2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I am in the main handler')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        count_template = JINJA_ENVIRONMENT.get_template("Templates/number.html")
        count_welcome = JINJA_ENVIRONMENT.get_template("Templates/number-start.html")
        self.response.write(count_welcome.render())
    def post(self):
        count_template = JINJA_ENVIRONMENT.get_template("Templates/number.html")
        users_fav_num = self.request.get("my_num")
        self.response.write(count_template.render(
        {"user_number": users_fav_num}
        ))


class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortune_template = JINJA_ENVIRONMENT.get_template("Templates/fortune.html")
        fortune_welcome = JINJA_ENVIRONMENT.get_template("Templates/fortune-start.html")
        fortunes = ['You will win the lottery', 'You will be a CSSI Fellow', 'You will meet your favorite celebrity']
        self.response.write(fortune_welcome.render())
    def post(self):
        fortune_template = JINJA_ENVIRONMENT.get_template("Templates/fortune.html")
        users_name = self.request.get("my_name")
        users_location = self.request.get("my_location")
        self.response.write(fortune_template.render(
        {"name": users_name,
        "location": users_location}
        ))

class GifHandler(webapp2.RequestHandler):
    def get(self):
        gif_welcome = JINJA_ENVIRONMENT.get_template("Templates/gif-form.html")
        self.response.write(gif_welcome.render())
    def post(self):
        user_query = self.request.get('user-query')
        url = "http://api.giphy.com/v1/gifs/search?q=" + user_query.replace(" ", "+") + "&api_key=dc6zaTOxFJmzC"
        data = urllib2.urlopen(url)
        giphy_json_content = data.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        image = parsed_giphy_dictionary['data'][0]['images']['fixed_height']['url']
        template = JINJA_ENVIRONMENT.get_template("Templates/gif-display.html")
        self.response.write(template.render({"gif": image}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fortune', FortuneHandler),
    ('/count', CountHandler),
    ('/gifs', GifHandler)
], debug=True)
