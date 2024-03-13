from flask import Blueprint, render_template

views = Blueprint('views', __name__)
# setting up blue print means that the file has a bunch of routes on its inside

@views.route('/') # a decorator
def home():
    #this function would run whenever we make type is '/' on the server
    return render_template("home.html")

@views.route('/about-app')
def about_us():
    return render_template("about_app.html")

