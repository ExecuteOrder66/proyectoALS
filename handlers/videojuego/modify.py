#Modificar videojuego
from time import sleep

import webapp2
from google.appengine.api import images
from webapp2_extras.users import users
from webapp2_extras import jinja2


from model.videojuego import Videojuego
from model.videojuego import Genero
from model.videojuego import Pegi


class ModificaVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            videojuego = Videojuego.recupera(self.request)

            valores_plantilla = {
                "videojuego": videojuego
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("modify_videojuego.html", **valores_plantilla))
        else:
            print("No esta loggeado en modify")
            return self.redirect("/")


    def post(self):
        print("-------------PUT MODIFY-----------")
        titulo = self.request.get("modTitulo", "falta titulo")
        sinopsis = self.request.get("modSinopsis", "")
        str_genero = self.request.get("modGenero", "")
        str_pegi = self.request.get("modPegi", "")
        data_caratula = self.request.get("modCaratula", None)

        #DEFINE GENERO DEL JUEGO
        genero = Genero.get(str_genero)

        print ("------------------------------------------")
        print("titulo: {0}"
              "sinopsis: {1}".format(titulo, sinopsis))
        print ("------------------------------------------")

        try:
            pegi = int(str_pegi)
            pegi = Pegi.get(pegi)

        except ValueError:
            pegi = -1

        print("WEA+++++++++++++++")
        #If comprobaciones, redirigir si algo va mal
        if not(titulo) or not(sinopsis) or not(genero) or pegi<0:
            print("ALGO VACIO")
            return self.redirect("/")
        else:
            print("**********MODIFICANDO****************")
            juego = Videojuego.recupera(self.request)

            if data_caratula:
                juego.caratula = images.resize(data_caratula, 220, 306)

            juego.titulo = titulo
            juego.sinopsis = sinopsis
            juego.genero = genero
            juego.pegi = pegi

            juego.put()
            sleep(1)
            return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/videojuego/modifica', ModificaVideojuegoHandler)
], debug=True)