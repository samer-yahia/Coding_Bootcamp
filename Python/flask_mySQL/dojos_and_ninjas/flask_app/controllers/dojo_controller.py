from flask import Flask, render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja 


@app.route('/dojos')
def dojo():
    context = {"all_dojos" : Dojo.get_all()}
    return render_template('dojo.html', **context)


@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def display_dojo(dojo_id):
    dict = {"id": dojo_id}
    return render_template('display_dojo.html', dojo = Dojo.get_one(dict))