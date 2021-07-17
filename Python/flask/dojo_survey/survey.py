from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')


@app.route('/results')
def display_result():
    return render_template('results.html')


if __name__=='__main__':
    app.run(debug=True)