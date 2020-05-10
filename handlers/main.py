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
from webapp2_extras.users import users

from model.videojuego import Videojuego
import model.user as user_model
import model.userlike as like_model


class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        user = user_model.retrieve(usr)

        if usr and user:
            usr_url = users.create_logout_url("/")
        else:
            user = user_model.create_empty_user()
            user.nick = "Login"

            usr_url = users.create_login_url("/")

        videojuegos = Videojuego.query().order()

        juegos_like = like_model.get_juegos_like(user.email)
        juegos_key_list = []
        for juego in juegos_like:
            juegos_key_list.append(juego.videojuego.urlsafe())

        print("juegos_key_list= {0}".format(juegos_key_list))

        valores_plantilla = {
            "videojuegos": videojuegos,
            "juegos_key_list": juegos_key_list,
            "usr": usr,
            "usr_url": usr_url,
            "user": user
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **valores_plantilla))





app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
