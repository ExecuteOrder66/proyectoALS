# Videojuego con su informacion

from google.appengine.ext import ndb


class Genero:
    ACCION = "ACCION"
    ESTRATEGIA = "ESTRATEGIA"
    PLATAFORMAS = "PLATAFORMAS"
    OTRO = "OTRO"

    @staticmethod
    def get(str_genero):
        if str_genero == "Accion":
            return Genero.ACCION
        elif str_genero == "Estrategia":
            return Genero.ESTRATEGIA
        elif str_genero == "Plataformas":
            return Genero.PLATAFORMAS
        else:
            return Genero.OTRO


class Pegi:
    DIECIOCHO = 18
    DIECISEIS = 16
    DOCE = 12
    SIETE = 7
    TRES = 3

    @staticmethod
    def get(codigo):
        if codigo==16:
            return Pegi.DIECISEIS
        elif codigo==12:
            return Pegi.DOCE
        elif codigo==7:
            return Pegi.SIETE
        elif codigo==3:
            return Pegi.TRES
        else:
            return Pegi.DIECIOCHO


class Videojuego(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    sinopsis = ndb.TextProperty(required=True)
    genero = ndb.StringProperty(required=True)
    #genero = Enum(["ACCION","ESTRATEGIA","PLATAFORMAS","OTRO"])
    #genero = Genero()
    pegi = ndb.IntegerProperty(required=True)
    caratula = ndb.BlobProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id=""

        #Devuelve clave
        return ndb.Key(urlsafe=id).get()
