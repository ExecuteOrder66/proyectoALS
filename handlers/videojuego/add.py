#Nuevo videojuego
from time import sleep

import webapp2
from google.appengine.api import images
from webapp2_extras import jinja2
from model.videojuego import Videojuego

from model.videojuego import Videojuego


class NuevoVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        videojuegos = Videojuego.query().order()


        valores_plantilla = {
            "videojuegos": videojuegos
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("add_videojuego.html", **valores_plantilla))


    def post(self):
        self.response.write("Formulario recibido, registrando videojuego")
        titulo = self.request.get("addTitulo", "falta titulo")
        sinopsis = self.request.get("addSinopsis", "")
        str_genero = self.request.get("addGenero", "")
        str_pegi = self.request.get("addPegi", "")
        caratula = self.request.get("addCaratula", "")

        genero = str_genero

        print ("------------------------------------------")
        print("titulo: {0}"
              "sinopsis: {1}".format(titulo, sinopsis))
        print ("------------------------------------------")

        try:
            pegi = int(str_pegi)

        except ValueError:
            pegi = -1

        #If comprobaciones, redirigir si algo va mal
        if not(titulo) or not(sinopsis) or not(genero) or pegi<0 or not(caratula):
            return self.redirect("/")
        else:
            juego = Videojuego(titulo=titulo, sinopsis=sinopsis, genero=genero, pegi=pegi, caratula=caratula)
            juego.put()
            sleep(1)
            return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/videojuego/nuevo', NuevoVideojuegoHandler)
], debug=True)