#!/usr/bin/python3

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer, requests, sys, io, cgitb
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
cgitb.enable()
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
sanitizer = html_sanitizer.Sanitizer()
scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()

form = cgi.FieldStorage()
if "your_name" in form:
    Id = form["your_name"].value
    pageId = sanitizer.sanitize(Id)
else:
    pageId = ''
    scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    meditation = ''

print('''<!doctype html>
<html>
<head>
    <title>321son Family - Meditation</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1><a href="index.py">Examining the Scriptures Daily</a></h1>
    <div id="today">
        <h2>{today_html}</h2>
        </div>
    <div id="scripture">
        <h2>{scripture_html}</h2>
        <p>{bodyText_html}</p>
    </div>
    <h2>{pageId_html}  [ {title_html} ]</h2>
    <form action="process_create_meditation.py" method="post">
        <input type="hidden" name="your_name" value="{form_name}">
        <p><textarea rows="20" cols="100%" name="meditation" placeholder="Please, write your meditation."></textarea></p>
        <p><input type="submit" value="저장"></p>
    </form>
    <div id="grid">
        <div id="list">
            <ul>{listStr_html}</ul>
        </div>
    </div>
</body>
</html>
'''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, pageId_html=pageId, title_html=RealDay, form_name=pageId, listStr_html=view.getDir()))
