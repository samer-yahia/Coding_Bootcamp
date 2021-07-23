from flask import Flask, render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja 


@app.route("/ninjas/new")
def new_ninja():
    context = {"all_dojos" : Dojo.get_all()}
    return render_template('create_ninja.html', **context)


@app.route('/ninjas/create/new', methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{dojo_id}')