from flask import Flask

def create_ap():
    app = Flask(__name__)
    app.config['SECRE_KEY'] = 'hkdalkkda kjagdlih'

    return app
