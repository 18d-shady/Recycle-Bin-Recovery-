from flask import render_template, request
import requests
import os
from app import app
from app import get


music = ".mp3"
rec = '$Recycle.Bin'

"""
for path, folder, files in os.walk("C://"):
    for file in files:
        if rec in path:
            filepath = os.path.join(path, file)
            #print(filepath)
            if ".mp3" in filepath:
            	print("Music "+ filepath)
            elif ".jpg" or ".png" in filepath:
            	print("pictures " + filepath)
            elif ".mp4" in filepath:
            	print("video " + filepath)
            else:
            	print("others " + filepath)
"""


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/music', methods=['GET','POST'])
def music():
	#session['url'] = url_for('music')
	choosen = request.form.get('restore')
	if not choosen:
		pass
	else:
		print(choosen)
		get.downloadIt(choosen)
	return render_template("music.html", shown = get.moosic)

@app.route('/picture', methods=['GET','POST'])
def picture():
	choosen = request.form.get('restore')
	if not choosen:
		pass
	else:
		print(choosen)
		get.downloadIt(choosen)
	return render_template("picture.html", shown = get.pikchar)

@app.route('/video', methods=['GET','POST'])
def video():
	choosen = request.form.get('restore')
	if not choosen:
		pass
	else:
		print(choosen)
		get.downloadIt(choosen)
	return render_template("video.html", shown = get.vido)

@app.route('/other', methods=['GET','POST'])
def other():
	choosen = request.form.get('restore')
	if not choosen:
		pass
	else:
		print(choosen)
		get.downloadIt(choosen)
	return render_template("other.html", shown = get.oda)


@app.route('/all', methods=['GET','POST'])
def allFiles():
	choosen = request.form.get('restore')
	if not choosen:
		pass
	else:
		print(choosen)
		get.downloadIt(choosen)
	return render_template("allFiles.html", shown = get.allFile)


@app.route('/system', methods=['GET','POST'])
def system():
	choosen = request.form.get('restore')
	if not choosen:
		pass
	else:
		print(choosen)
		get.downloadIt(choosen)
	return render_template("system.html", shown = get.sistem)	

