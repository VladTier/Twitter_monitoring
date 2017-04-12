from flask import Blueprint, jsonify, render_template, request, redirect, url_for, \
    session, flash
from passlib.hash import sha256_crypt
from flask_login import login_user, LoginManager, login_required, current_user

from forms import WordsForm, LoginForm, RegisterForm
from extensions import db
from models_db import Users, Words, Tweets

login_manager = LoginManager()



@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter(Users.id == int(user_id)).first()

page_view = Blueprint('page_view', __name__)



@page_view.route('/find', methods=['GET', 'POST'])
@login_required
def index():
    """Create welcome page"""
    form = WordsForm(request.form)
    user = current_user
    if request.method == 'POST':
        if form.validate_on_submit():
            word = Words(
                word=form.words.data)

            user.words_table.append(word)
            db.session.add(user)
            db.session.commit()
            flash('Looking for tweets with ' + word.word)

    return render_template('find.html', form=form)


@page_view.route('/words', methods=['GET'])
def words():
    if request.method == 'GET':
        results = Users.query.all()
        json_result = {'word': results.words}
        return jsonify(items=json_result)

#Add endpoint to fetch a list of all tracked words


@page_view.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=request.form['username']).first()
        if user is not None and sha256_crypt.verify(request.form['password'],
                                                    user.password):

            login_user(user)
            flash('Logged in successfully.')

            return redirect('/find')
        else:
            error = 'Invalid username or password.'

    return render_template('login.html', form=form, error=error)



"""
# @page_view.route('/login', methods=['GET','POST'])
# def login():
#     error = None
#     form = LoginForm(request.form)
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             user = Users.query.filter_by(username = request.form['username']).first()
#             if user is not None and sha256_crypt.verify(request.form['password'], user.password):
#                 flash('You were logged in')
#
#                 session['logged_in'] = True
#                 return redirect('/find')
#             else:
#                 error = 'Invalid username or password.'
#     return render_template('login.html', form=form, error=error)
"""

@page_view.route('/logout')
@login_required
def logout():
    """create logout page"""
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('page_view.login'))


@page_view.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(email=request.form['email']).first()
        if user:
            flash('That email is already taken, please choose another')
            return redirect('/registration')
        else:
            user = Users(
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=sha256_crypt.encrypt(form.password.data),
                username=form.username.data,
            )
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect('/find')

    return render_template('registration.html', form=form)

