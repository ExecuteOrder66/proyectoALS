# Videojuego con su informacion

from google.appengine.ext import ndb

class Videojuego(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    sinopsis = ndb.TextProperty(required=True)
    genero = ndb.StringProperty(required=True)
    pegi = ndb.IntegerProperty(required=True)
    caratula = ndb.BlobProperty(required=True)