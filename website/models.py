from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#FOR THIS APPLICATION, WE DEFINE ALL THE DATABASE MODEL/ TABLE WE WOULD BE USING.

#importing from the current package (website folder) the db
# could have been from website import db

# the UserMixin class is inherted to help manage user authentincation.
# it adds several methods and properties that are commonly used in Flask applications for managing user authentication.

# these properties and methods includes:
# is_authenticated, is_active, is_anonymous, get_id()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # by default database sets id for me.
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # func.now() gets the current date and time without needing me to make edits

    # associating our notes with the different users. 
    # (setting up a relationship between the notes objects and user objects)
    # i do this in the form of a foreign key.
    # foreign key is a key on one of my database that references an id to another database column.

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # the above defines one to many relationship
    # one user with many notes.
    # install foreign key on the child objects that identifies the parent object.
    # user.id because the User class is represented as just user in sql database.
    # and the id is simply the unique identifier of the other database.

# DEFINING A SCHEMA FOR MY USER
# a schema is a blueprint for an object to be stored in adatabase
class User(db.Model, UserMixin): # inheriting the db.Model and UserMixin class.
    id = db.Column(db.Integer, primary_key=True) # using a primary key ->a unique value
    email = db.Column(db.String(150), unique=True) # maximum length of value is 150
    # the unique property also ensures that no user has the same email as another
    # it becomes invalid to have a repeated email as a login information
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    # with this a list with all the notes related to the user is being stored)


