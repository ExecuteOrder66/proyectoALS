#Nuevo videojuego
from time import sleep

import webapp2
from google.appengine.api import images
from webapp2_extras.users import users
from webapp2_extras import jinja2


from model.videojuego import Videojuego
from model.videojuego import Genero
from model.videojuego import Pegi
import model.user as user_model


class NuevoVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            videojuegos = Videojuego.query().order()

            valores_plantilla = {
                "videojuegos": videojuegos
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("add_videojuego.html", **valores_plantilla))
        else:
            print("No esta loggeado en add")
            return self.redirect("/")



    def post(self):
        self.response.write("Formulario recibido, registrando videojuego")
        titulo = self.request.get("addTitulo", "falta titulo")
        sinopsis = self.request.get("addSinopsis", "")
        str_genero = self.request.get("addGenero", "")
        str_pegi = self.request.get("addPegi", "")
        data_caratula = self.request.get("addCaratula", None)
        usr = users.get_current_user()
        user = user_model.retrieve(usr)


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

        #If comprobaciones, redirigir si algo va mal
        if not(titulo) or not(sinopsis) or not(genero) or pegi<0 or not(data_caratula) or not(user):
            return self.redirect("/")
        else:
            juego = Videojuego(titulo=titulo, sinopsis=sinopsis, genero=genero, pegi=pegi, caratula=data_caratula, usr_email=user.email)
            juego.caratula = images.resize(data_caratula, 220, 306)
            juego.put()
            sleep(1)
            return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/videojuego/nuevo', NuevoVideojuegoHandler)
], debug=True)