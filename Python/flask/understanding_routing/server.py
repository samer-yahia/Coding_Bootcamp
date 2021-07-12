from flask import Flask

app = Flask(__name__)

# main page seen when accessing website
@app.route('/')
def index():
    return 'Hello World!'

# displays Dojo
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Contains variable name that will display user's name if inputted
@app.route('/say/<name>')
def greeting(name):
    return f'hi {name}'

# Contains function that will display a phrase a number of times
@app.route('/repeat/<int:num>/<var>')
def repeater(num,var):
    return num * f'{var}'


if __name__=='__main__':
    app.run(debug=True)