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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I am in the main handler')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I am the CountHandler')

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortunes = ['You will win the lottery', 'You will be a CSSI Fellow', 'You will meet you meet your favorite celebrity']
        self.response.write(fortunes[random.randrange(0,2)])

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/fortune', FortuneHandler)
], debug=True)