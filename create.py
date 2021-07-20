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

# pageId = ''
# your_name = ''
# pageId = sanitizer.sanitize(pageId)
# your_name = sanitizer.sanitize(your_name)

print('''<!doctype html>
<html>
<head>
  <title>321son Family - ID 생성</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1><a href="index.py">Examining the Scriptures Daily</a></h1>
  <div id="today">
    <h2>{today_html}</h2>
    <h2>Welcome to 321son Family</h2>
  </div>
  <div id="list">
    <ul>{listStr_html}</ul>
  </div>
  <form action="process_create.py" method="post">
    <p><input type="text" size="50" name="your_name" placeholder="영문 이름을 쓰세요."></p>
    <input type="submit" value="제출">
  </form>
</body>
</html>
'''.format(today_html=RealDay, listStr_html=view.getMeditation()))
