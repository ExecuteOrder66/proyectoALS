from google.appengine.ext import ndb
from google.appengine.api import users



class User(ndb.Model):

    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    email = ndb.TextProperty(indexed=True)
    nick = ndb.TextProperty(indexed=True)

    def __str__(self):
        return " (" + self.email + ")"

    def __unicode__(self):
        return ": " + self.nick + " (" + self.email + ")"

def create(usr):
    """Creates a new user object, from GAE's user object.
        :param usr: The GAE user object.
        :return: A new User object."""
    toret = User()

    toret.email = usr.email()
    toret.nick = usr.nickname()

    return toret


def create_empty_user():
    """Used when there the user is not important."""
    return User(email="", nick="")


@ndb.transactional
def update(user):
    """Updates a user.
        :param user: The user to update.
        :return: The key of the record.
    """
    return user.put()


def retrieve(usr):
    """Reads the user info from the database.
    :param usr: The GAE user object.
    :return: The User retrieved, or a client created appropriately if not found.
    """
    toret = None

    if usr:
        usr_email = usr.email()
        found_users = User.query(User.email == usr_email).order(-User.added)

        if found_users.count() == 0:
            toret = create(usr)
            update(toret)
        else:
            toret = found_users.iter().next()
            toret.usr = usr

    return toret