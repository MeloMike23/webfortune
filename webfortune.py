from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('fortune')

@app.route('/fortune/')
def fortune():
	os.system('fortune')

@approute('/cowsay/<message>/')
def cowsay(message):
	os.system('cowsay' + message)
	

@app.route('/cowfortune/')
def cowfortune():
	os.system('fortune | cowsay')
