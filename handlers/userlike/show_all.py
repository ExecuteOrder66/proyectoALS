import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.videojuego import Videojuego
import model.user as user_model
import model.userlike as like_model


class ListaLikeHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        user = user_model.retrieve(usr)

        if usr and user:
            juegos_like = like_model.get_juegos_like(user.email)
            videojuegos = Videojuego.query().order()
            keys_fav = []
            for userlike in juegos_like:
                keys_fav.append(userlike.videojuego.urlsafe())

            valores_plantilla = {
                "keys_fav": keys_fav,
                "videojuegos": videojuegos,
                "usr": usr,
                "user": user
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("show_all_likes.html", **valores_plantilla))
        else:
            print("else show all likes, redireccionando")
            return self.redirect("/")









app = webapp2.WSGIApplication([
    ('/like/lista', ListaLikeHandler),
], debug=True)