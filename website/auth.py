from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

from . import db

from werkzeug.security import generate_password_hash, check_password_hash
# the above imports an hashing mechanism that helps hashing the password.
# a hashing function is a one-way function THAT DOES NOT HAVE AN INVERSE.
# the password is never stored in plain text

from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# the methods list tells what methods is permitted at the endpoint
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # query and confirm entry in database
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                #remebers user is logged in until cookies is cleared
                login_user(user, remember=True)

                # redirect to home page after successful login
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required    # JUST TO ENSURE THAT THE LOGOUT FUNCTION DOES NOT WORK IF THERE IS NO LOGIN
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # confirm and ensure that a signup email is not repeated
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
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

            # remeber the user is logged in 
            login_user(new_user, remember=True)

            # flash a success message
            flash('Account created!', category='success')

            # redirect the user to the homepage of the website
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
# the return statement above simply ensures the current_user object can be used in the sign up template. it is useful to display information about the current user on the sign-up page of customizing the page based on the user's authentication status or role
