import os
import shutil
from datetime import datetime


rec = 'Recycle.Bin'
moosic = ''
pikchar = ""
vido = ""
oda = ""
allFile = ""
sistem = ""
counter = 0
curr_direc = os.getcwd()

def makeFolder(pathss):
	if os.path.exists(pathss):
		pass
	else:
		os.mkdir(pathss)

makeFolder(curr_direc + "/Restored/")
makeFolder(curr_direc + "/Restored/Music/")
makeFolder(curr_direc + "/Restored/Picture/")
makeFolder(curr_direc + "/Restored/Video/")
makeFolder(curr_direc + "/Restored/Other/")



for path, folder, files in os.walk("C://$Recycle.Bin/"):
    for file in files:
        if rec in path and "$" not in file:
        	allFile += "<button class='tooltipp' type='Submit' name='restore' value="+file+">"+file+"<span class='tooltiptext'>Restore</span></button>"
        	if ".mp3" in file:
        		#moosic += f"<label for='Restore Music{counter}' >" + file + f"</label>\n<input class='buttons' type='Submit' id='Restore Music{counter}' name='restore' value='Restore Music{counter}'>"
        		moosic += "<button class='tooltipp' type='Submit' name='restore' value="+file+">"+file+"<span class='tooltiptext'>Restore</span></button>"

        	elif ".jpg" in file or ".png" in file:
        		#moosic += f"<label for='Restore Music{counter}' >" + file + f"</label>\n<input class='buttons' type='Submit' id='Restore Music{counter}' name='restore' value='Restore Music{counter}'>"
        		pikchar += "<label class='tooltipp'><input type='radio' name='restore' value="+file+" onchange='this.form.submit()' /><img src='" + os.path.join(path, file) + "' alt='" + file + " cant show' /><span class='tooltiptext'>Restore</span></label>" 
 

        	elif ".mp4" in file or ".m4" in file:
        		#moosic += f"<label for='Restore Music{counter}' >" + file + f"</label>\n<input class='buttons' type='Submit' id='Restore Music{counter}' name='restore' value='Restore Music{counter}'>"
        		vido += "<button class='tooltipp' type='Submit' name='restore' value="+file+">"+file+"<span class='tooltiptext'>Restore</span></button>"
  

        	else:
        		#moosic += f"<label for='Restore Music{counter}' >" + file + f"</label>\n<input class='buttons' type='Submit' id='Restore Music{counter}' name='restore' value='Restore Music{counter}'>"
        		oda += "<button class='tooltipp' type='Submit' name='restore' value="+file+">"+file+"<span class='tooltiptext'>Restore</span></button>"

        elif rec in path and "$" in file:
        	sistem += "<button class='tooltipp' type='Submit' name='restore' value="+file+">"+file+"<span class='tooltiptext'>Restore</span></button>"

    


 

def downloadIt(rfile):
	for path, folder, files in os.walk("C://$Recycle.Bin/"):
	    for file in files:
	        if rec in path:
	        	if 'mp3' in rfile:
		        	if rfile == file:
		        		#curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
		        		target = curr_direc + rf"/Restored/Music/restored {file}"
		        		shutil.copyfile(os.path.join(path, file), target)

		        elif 'jpg' in rfile:
		        	if rfile == file:
		        		#curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
		        		target = curr_direc + rf"/Restored/Picture/restored {file}"
		        		shutil.copyfile(os.path.join(path, file), target)

		        elif 'mp4' in rfile:
		        	if rfile == file:
		        		#curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
		        		target = curr_direc + rf"/Restored/Video/restored {file}"
		        		shutil.copyfile(os.path.join(path, file), target)

		        else:
		        	if rfile == file:
		        		#curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
		        		target = curr_direc + rf"/Restored/Other/restored {file}"
		        		shutil.copyfile(os.path.join(path, file), target)


#print(moosic)
"""
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