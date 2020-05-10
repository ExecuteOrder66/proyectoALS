import webapp2
import time
from webapp2_extras.users import users

from model.videojuego import Videojuego
from model.userlike import UserLike
import model.user as user_model
import model.userlike as user_like


class AddModifyLikeHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        user = user_model.retrieve(usr)

        if usr and user:
            like = UserLike()
            like.usr_email = user.email
            like.videojuego = Videojuego.recupera(self.request).key

            if user_like.can_be_created_like(like):
                print("Like dado")
                time.sleep(1)
                return self.redirect("/")
            elif user_like.can_delete_like(like):
                print("Like borrado")
                time.sleep(1)
                return self.redirect("/")
            else:
                print("no se pudo insertar o eliminar like")
                time.sleep(1)
                return self.redirect("/")
        else:
            print("Volviendo a la raiz, user no identificado en add_modify like")
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/like/modifica', AddModifyLikeHandler),
], debug=True)
