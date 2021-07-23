from flask import render_template, sessions, redirect, request

from flask_app.models.author import author
from flask_app.models.book import book


# 
@app.route('/')
def author_index():
    return render_template('index.html')


