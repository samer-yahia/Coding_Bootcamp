from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt 

from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


bcrypt = Bcrypt(app)


@app.route('/')
def index():
    # session.clear()
    if "uuid" in session:
        return redirect('/dashboard')

    return render_template('index.html')

@app.route('/register/validate', methods = ['POST'])
def register_user():
    if not User.valid_register(request.form):
        return redirect('/')
    
    hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": hash
    }
    user_id = User.create(data)

    session["uuid"] = user_id

    return redirect("/dashboard")

@app.route('/login', methods = ['POST'])
def login():
    if not User.valid_login(request.form):
        return redirect('/')
    
    user = User.get_email({'email': request.form['email']})
    session['uuid'] = user.id

    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


