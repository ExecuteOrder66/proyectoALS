#Lista de videojuegos que le gustan a un usuario

from google.appengine.ext import ndb
from videojuego import Videojuego

class Lista(ndb.Model):
    usr = ndb.StringProperty
    videojuego = ndb.KeyProperty(kind=Videojuego)