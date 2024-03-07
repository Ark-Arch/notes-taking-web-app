from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hkdalkkda kjagdlih'
    # the key above is responsible for encrypting the cookies/session data associated with the application.

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # url_prefix is used to prefix what ever is defined as the route link

    return app
