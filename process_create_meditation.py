#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

import cgi, os, view, html_sanitizer, requests, sys, io
from datetime import datetime, timedelta

sanitizer = html_sanitizer.Sanitizer()
day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)

form = cgi.FieldStorage()
Id = form["your_name"].value
pageId = sanitizer.sanitize(Id)
m = form["meditation"].value
meditation = sanitizer.sanitize(m)

root = 'data/'+pageId
file = os.listdir(root)
if RealDay in file:
    pass
else:
    opened_file = open(root+'/'+RealDay, 'w', encoding='UTF-8')
    opened_file.write(meditation)
    opened_file.close()


#Redirection
print("Location: meditation.py?id="+pageId)
print()
