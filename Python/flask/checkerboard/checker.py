from flask import Flask, render_template

app = Flask(__name__)


# Each app route has variables within it to go back to the default 8x8 red/black board
# The intial board
@app.route('/')
def call_Board(y=8,x=8,color1='red',color2='black'):
    return render_template('index.html', y=y, x=x,color1=color1,color2=color2)


# Changes the number of columns
@app.route('/<int:y>')
def custom_Column(y=4,x=8,color1='red',color2='black'):
    return render_template('index.html', y=y, x=x,color1=color1,color2=color2)


# Changes the number of columns and rows
@app.route('/<int:y>/<int:x>')
def custom_Size(y=8, x=8,color1='red',color2='black'):
    return render_template("index.html", y=y, x=x,color1=color1,color2=color2)


# Changes the number of columns/rows and the colors of the board
@app.route('/<int:y>/<int:x>/<string:color1>/<string:color2>')
def custom_Color(y=8, x=8, color1='red',color2='black'):
    return render_template("index.html", y=y, x=x, color1= color1,color2=color2)


if __name__ =='__main__':
    app.run(debug = True)
