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
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.videojuego import Videojuego


class MainHandler(webapp2.RequestHandler):
    def get(self):
        videojuegos = Videojuego.query().order()


        valores_plantilla = {
            "videojuegos": videojuegos
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **valores_plantilla))


class Image(webapp2.RequestHandler):
    def get(self):
        videojuego_key = ndb.Key(urlsafe=self.request.get('img_id'))
        videojuego = videojuego_key.get()
        if videojuego.caratula:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(videojuego.caratula)
        else:
            self.response.out.write('No image')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/img', Image)
], debug=True)
