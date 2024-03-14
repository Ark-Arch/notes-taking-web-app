from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)
# setting up blue print means that the file has a bunch of routes on its inside

@views.route('/') # a decorator
@login_required # now i can not get to the home page unless i login
def home():
    #this function would run whenever we make type is '/' on the server
    return render_template("home.html", user=current_user)

@views.route('/about-app')
def about_us():
    return render_template("about_app.html")

