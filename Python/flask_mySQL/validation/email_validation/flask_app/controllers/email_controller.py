from flask import render_template, redirect, request, session

from flask_app.models.email import Email


@app.route('/')
def create_email():
    return render_template('index.html')
