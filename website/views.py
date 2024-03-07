from flask import Blueprint

views = Blueprint('views', __name__)
# setting up blue print means that the file has a bunch of routes on its inside

@views.route('/') # a decorator
def home():
    #this function would run whenever we make type is '/' on the server
    return "<h1>TEST</h1>"
