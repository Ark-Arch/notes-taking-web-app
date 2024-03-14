from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() # a database object created
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hkdalkkda kjagdlih'
    # the key above is responsible for encrypting the cookies/session data associated with the application.

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # note that for the above line of code:
    # it defines the appropriate URI of the database intended for use.
    # URI -> Uniform Resource Identifier.
    # it is the value of the URI that specifies the database connection details.
    # notice the URI indicates that we are using SQLite as the database engine.
    # and that database.db is the name of the SQLite database file.
    # i could replace sqlite:/// with mysql:// or postgressql://


    db.init_app(app) # this ties the database to this flask application.

    # note that . indicates the current directory.
    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # url_prefix is used to prefix what ever is defined as the route link

    from .models import User, Note
    # this is to make sure that we load the models file and define the User and Note classes before initializing our databases.

    with app.app_context():
        db.create_all()

    return app
