#Nuevo videojuego
from time import sleep

import webapp2
from google.appengine.api import images
from webapp2_extras.users import users
from webapp2_extras import jinja2


from model.videojuego import Videojuego
from model.videojuego import Genero
from model.videojuego import Pegi


class EliminaVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            videojuego = Videojuego.recupera(self.request)
            videojuego.key.delete()
            sleep(1)

            return self.redirect("/")
        else:
            print("No esta loggeado en delete")
            return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/videojuego/elimina', EliminaVideojuegoHandler)
], debug=True)