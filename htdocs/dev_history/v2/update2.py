#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer, requests, sys, io
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

t = datetime.today()+timedelta(1)
y = str(t.year)
m = str(t.month).zfill(2)
d = str(t.day).zfill(2)
today = y+'/'+m+'/'+d
url = 'https://wol.jw.org/ko/wol/h/r8/lp-ko/'+ today
day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
sanitizer = html_sanitizer.Sanitizer()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    s = soup.find_all('p', {'class' : 'themeScrp'})
    scripture = s[0].text
    bt = soup.find_all('div', {'class' : 'bodyTxt'})
    bodyText = bt[0].text
    title = sanitizer.sanitize(pageId)
    m = open('data/'+pageId, 'r').read()
    meditation = sanitizer.sanitize(m)
else:
    pageId = 'Daily Text'
    meditation = 'Hello World!'

print('''<!doctype html>
<html>
<head>
  <title>Lee's Family - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><strong><a href="index.py">Examining the Scriptures Daily</a></strong></h1>
  <h2><strong>{today_html}</strong></h2>
  <h2><font color="#576cee"><em>{scripture_html}</em></font></h2>
  <p>{bodyText_html}</p>
  <h2><font color="purple">{title_html}</font></h2>
  <form action="process_update.py" method="post">
      <input type="hidden" name="pageId" value="{form_pageId}">
      <input type="hidden" name="title" value="{form_title}">
      <p><textarea rows="20" cols="100%" name="meditation" placeholder="Meditation">{form_default_meditation}</textarea></p>
      <p><input type="submit" value="제출"></p>
  </form>
  <ul>
    <font color = "red">
        {listStr_html}
    </font color>
  </ul>
</body>
</html>
'''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, title_html=title, form_pageId=pageId, form_title=title, form_default_meditation=meditation, listStr_html=view.getList()))
