#!/user/bin/python3

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer, requests, sys, io, pymysql, cgitb, glob
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
cgitb.enable()

day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
sanitizer = html_sanitizer.Sanitizer()
scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()

form = cgi.FieldStorage()
Id = form["id"].value
pageId = sanitizer.sanitize(Id)
title = pageId+'   ['+RealDay+']'
root = 'data/'+pageId
file = os.listdir(root)
if RealDay in file:
    m = open(root+'/'+RealDay, 'r', encoding='UTF-8').read()
else:
    m = '아직 묵상을 기록하지 않았네요. 이제 묵상한 내용을 기록해 봅시다.~~'
meditation = sanitizer.sanitize(m)

create_meditation = view.createMeditation(pageId)
update_action = ''
delete_action = ''


print('''<!doctype html>
<html>
    <head>
      <title>321son Family - Welcome</title>
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
      <div id="grid">
          <div id="Daily_Text">
            <h2>{title_html}</h2>
            <div id="meditation">
                <p>{meditation_html}</p>
            </div>
          </div>
          <div id="list">
            <ul>{listStr_html}</ul>
          </div>
      </div>
      {create_action}
      {update_action}
      {delete_action}
    </body>
</html>
 '''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, title_html=title, meditation_html=meditation, listStr_html=view.getPersonalList(), create_action=create_meditation, update_action=update_action, delete_action=delete_action))
