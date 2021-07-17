from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"


@app.route('/')
def index():
    context = {"all_users": User.get_all()}
    return render_template('index.html', **context)


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')


@app.route('/users/create', methods = ['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)