from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.account import Account

bcrypt = Bcrypt(app)


@app.route('/')
def reg_and_log():
    if "uuid" in session:
        return redirect('/accounts')
    return render_template('index.html')


@app.route('/accounts', methods = ['POST'])
def display_users():
    if "uuid" not in session:
        flash('Must Log In')
        return redirect('/')
    return render_template('accounts.html', all_users = Account.get_all, user = Account.get_id({"id": session['uuid']}))


@app.route('/register', methods = ['POST'])
def register():
    if not Account.valid_register(request.form):
        return redirect('/')
    
    hash = bcrypt.generator_password_hash(reqeust.form['password'])
    data = {
        **request.form,
        'password': hash
    }

    user_id = Account.create(data)
    session['uuid'] = user_id

    return redirect('/accounts.html')


@app.route('/login', methods = ['POST'])
def login_validate(post_data):
    if not Account.login_validate(request.form):
        return redirect('/')

    user = User.get_email({"email": request.form['email']})
    session['uuid'] = user.id

    return redirect('/accounts')


@app.route('/logout')
def logout():
    session.clear()
    
    return redirect('/')