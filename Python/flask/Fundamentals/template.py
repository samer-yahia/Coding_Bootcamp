from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)