from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/play')
# def add_box():
#     render_template('index.html')

# @app.route('/play/<int:x>')
# def num_box(x):
#     return render_template('index.html', x=x)

@app.route('/')
@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def color_boxes(x=3, color='lightblue'):
    return render_template('index.html', x=x, color=color)

if __name__=='__main__':
    app.run(debug=True)