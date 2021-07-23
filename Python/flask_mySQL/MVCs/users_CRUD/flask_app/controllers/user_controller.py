from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

# Displays all users on home page
@app.route('/users')
def users():
    context = {"all_users": User.get_all()}
    return render_template('index.html', **context)


# Next two app routes creates user and retrieves the data
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')


@app.route('/users/create', methods = ['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')


# Display one user
@app.route('/users/display/<int:id>')
def display(id):
    dict = {"id": id}
    return render_template('display_user.html', user = User.get_one(dict))


#Edits one user
@app.route('/users/<int:id>/edit')
def edit_form(id):
    dict = {"id": id}
    return render_template('edit_user.html', user = User.get_one(dict))


@app.route('/users/<int:id>/complete', methods = ['POST'])
def edit_finish(id):
    dict = {'id': id, **request.form}
    User.update(dict)
    return redirect(f'/users/display/{id}')


# Deletes a user from the database
@app.route('/users/<int:id>/destroy')
def delete(id):
    dict = {'id': id}
    User.delete(dict)
    return redirect('/users')
