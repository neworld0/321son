#!/usr/bin/python3


import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
meditation = form["meditation"].value

opened_file = open('data/'+pageId, 'w')
opened_file.write(meditation)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
