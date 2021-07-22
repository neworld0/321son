#!/user/bin/python3

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer, requests, sys, io
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
sanitizer = html_sanitizer.Sanitizer()
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    title = sanitizer.sanitize(pageId)
    m = open('data/'+pageId, 'r').read()
    meditation = sanitizer.sanitize(m)
else:
    pageId = ''
    scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    title = ''
    meditation = ''

print('''<!doctype html>
<html>
<head>
  <title>Lee's Family - Welcome</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1><strong><a href="index.py">Examining the Scriptures Daily</a></strong></h1>
  <h2>{today_html}</h2>
  <h2>{scripture_html}</h2>
  <p>{bodyText_html}</p>
  <h2>{title_html}</h2>
  <form action="process_update.py" method="post">
      <input type="hidden" name="pageId" value="{form_pageId}">
      <input type="text" size=50 name="title" value="{form_title}">
      <p><textarea rows="20" cols="100%" name="meditation" placeholder="Meditation">{form_default_meditation}</textarea></p>
      <p><input type="submit" value="제출"></p>
  </form>
  <ul>
    {listStr_html}
  </ul>
</body>
</html>
'''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, title_html=title, form_pageId=pageId, form_title=title, form_default_meditation=meditation, listStr_html=view.getDir()))
