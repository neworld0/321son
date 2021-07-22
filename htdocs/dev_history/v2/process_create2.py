#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

import cgi
form = cgi.FieldStorage()
title = form["title"].value
meditation = form["meditation"].value
opened_file = open('data/'+title, 'w')
opened_file.write(meditation)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
