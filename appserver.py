
from flask import Flask, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('fortune')

@app.route('/fortune/')
def fortune():
	out = subprocess.run(['fortune'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	res = out.stdout.decode("utf-8")
	return '<pre>'+res+'</pre>'

@approute('/cowsay/<message>/')
def cowsay(message):
	moo = 'cowsay' + message
	out = subprocess.run([moo], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	res = out.stdout.decode("utf-8")
	return '<pre>'+res+'</pre>'
	

@app.route('/cowfortune/')
def cowfortune():
	outf = subprocess.run(['fortune'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	outc = subprocess.run(['cowsay'], input=outf.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	res = cow.stdout.decode("utf-8")
	return '<pre>'+res+'</pre>'
