#Lista de videojuegos que le gustan a un usuario

from google.appengine.ext import ndb
from videojuego import Videojuego

class UserLike(ndb.Model):
    usr_email = ndb.StringProperty(indexed=True)
    videojuego = ndb.KeyProperty(kind=Videojuego, required=True)


    @staticmethod
    def recupera(req):

        try:
            id = req.GET["id"]
        except KeyError:
            id=""

        return ndb.Key(urlsafe=id).get()


def can_be_created_like(like):
    query = UserLike.query(UserLike.usr_email == like.usr_email, UserLike.videojuego == like.videojuego).get()
    if query is None:
        like.put()
        return True
    else:
        return False


def can_delete_like(like):
    query = UserLike.query(UserLike.usr_email == like.usr_email, UserLike.videojuego == like.videojuego).get()
    if query is not None:
        query.key.delete()
        return True
    else:
        return False


def get_juegos_like(email):
    return UserLike.query(UserLike.usr_email == email)