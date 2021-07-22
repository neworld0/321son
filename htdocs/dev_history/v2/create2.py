#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html")
print()

import cgi, os, view, html_sanitizer, requests, sys, io
from datetime import datetime, timedelta

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

today = datetime.today()
RealDay = str(today.year)+'-'+str(today.month).zfill(2)+'-'+str(today.day).zfill(2)

sanitizer = html_sanitizer.Sanitizer()
form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    m = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(title)
    meditation = sanitizer.sanitize(m)
else:
    pageId = 'Daily Text'
    meditation = 'Hello World!'

print('''<!doctype html>
<html>
<head>
  <title>321son Family - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><strong><a href="index.py">Examining the Scriptures Daily</a></strong></h1>
  <h2><strong>{today_html}</strong></h2>
  <ul><strong><font color = "red">{listStr_html}</font color></strong></ul>
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="이름을 쓰세요."></p>
    <p><textarea rows="10" cols="100%" name="meditation" placeholder="묵상한 내용을 쓰세요."></textarea></p>
    <input type="submit" value="제출">
  </form>
</body>
</html>
'''.format(today_html=RealDay, listStr_html=view.getList()))
