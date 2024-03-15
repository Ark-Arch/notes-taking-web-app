from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)
# setting up blue print means that the file has a bunch of routes on its inside

@views.route('/', methods=['GET', 'POST']) # a decorator
@login_required # now i can not get to the home page unless i login
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    #this function would run whenever we make type is '/' on the server
    return render_template("home.html", user=current_user)

@views.route('/previous-notes')
@login_required
def previous_notes():
    data = dir(request)
    print(data)
    d = request.content_length
    print(d)
    return render_template("previous_notes.html", user=current_user)

@views.route('/about-app')
def about_us():
    return render_template("about_app.html")

# this would only take on the POST method. no GET request
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId) # access primary key
    if note:
        if note.user_id == current_user.id: # if the user signed in owns the note,
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({}) # returns an empty response, because we NEED TO return something from these views or routes
