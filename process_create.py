#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

import cgi, os, cgitb
cgitb.enable()

form = cgi.FieldStorage()
title = form["your_name"].value
opened_directory = os.makedirs('data/'+title)

#Redirection
print("Location: create.py")
print()
