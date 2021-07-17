from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

@app.route('/')
def index():
    if 'count' not in session:
        session['count']= 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/end_function')
def end_function():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug= True)
