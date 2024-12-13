from flask import Flask,render_template
from random import randint

app = Flask(__name__)

hero = ['1','2','3','4','5','6','7','8']

@app.route('/index')
def index():
    return render_template('index.html',hero1 = hero)

@app.route('/choujiang')
def choujiang():
    num = randint(0,len(hero))
    return render_template('index.html',hero1 = hero,h= hero[num])

app.run(debug=True)
