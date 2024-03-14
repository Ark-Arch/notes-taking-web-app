from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

from . import db

from werkzeug.security import generate_password_hash, check_password_hash
# the above imports an hashing mechanism that helps hashing the password.
# a hashing function is a one-way function THAT DOES NOT HAVE AN INVERSE.
# the password is never stored in plain text


auth = Blueprint('auth', __name__)

# the methods list tells what methods is permitted at the endpoint
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "this is the logout foett"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        else:
            # define the user
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))

            # add the user account to the database
            db.session.add(new_user)

            # make a commit to the database -> update the database
            db.session.commit()

            # flash a success message
            flash('Account created!', category='success')

            # redirect the user to the homepage of the website
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
