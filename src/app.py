from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('public/index.html')

@app.route("/educacao")
def educacao():
    return render_template('public/educacao.html')

@app.route("/portfolio")
def portfolio():
    return render_template('public/portfolio.html')

@app.route("/contatos")
def contatos():
    return render_template('public/contatos.html')