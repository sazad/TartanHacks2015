from __future__ import print_function
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/emojis")
def emojis():
	return render_template('emojis.html')

@app.route("/submitted", methods = ["POST"])
def submitted() :
	given = request.form['input']	
	images = translate(given)
	return render_template('display.html', images = images)


def translate(input):
	skipWords = ['the', 'and', 'or', 'a', 'an', 'aboard',
'about',
'across',
'after',
'against',
'along',
'amid',
'among',
'anti',
'around',
'as',
'at',
'behind',
'below',
'beneath',
'beside',
'besides',
'between',
'beyond',
'but',
'by',
'concerning',
'considering',
'despite',
'during',
'except',
'excepting',
'excluding',
'following',
'in',
'inside',
'into',
'near',
'of',
'off',
'on',
'onto',
'opposite',
'outside',
'over',
'past',
'per',
'plus',
'regarding',
'round',
'save',
'since',
'than',
'through',
'to',
'toward',
'towards',
'underneath',
'unlike',
'until',
'upon',
'versus',
'via',
'with',
'within',
'without']
	images = []
	words = input.split(" ")
	for w in words :
		if w not in skipWords:
			images.append(searchImage(w))
	return images


def searchImage(word):
	directory = "static"
	for file in os.listdir(directory):
		keywords = file.replace(".", " ").split(" ")
		if word in keywords:
			return file
	return "none"

if __name__ == "__main__":
    app.run(debug=True)
