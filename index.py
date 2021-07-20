#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer, requests, sys, io, pymysql, cgitb
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
cgitb.enable()

day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    id = form["id"].value
    m = open('data/'+id, 'r', encoding='UTF-8').read()
    pageId = sanitizer.sanitize(id1)
    title = RealDay

    list_scrp = os.listdir('copy_scripture')
    if RealDay in list_scrp:
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        parser = view.parser()
        s = parser.find_all('p', {'class' : 'themeScrp'})
        scrip = s[0].text
        opened_list_scrp = open('copy_scripture/'+RealDay, 'w', encoding='UTF-8')
        opened_list_scrp.write(scrip)
        opened_list_scrp.close()
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()

    list_body = os.listdir('copy_bodytext/')
    if RealDay in list_body:
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        parser = view.parser()
        bt = parser.find_all('div', {'class' : 'bodyTxt'})
        body = bt[0].text
        opened_list_body = open('copy_bodytext/'+RealDay, 'w', encoding='UTF-8')
        opened_list_body.write(body)
        opened_list_body.close()
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()

    create_action = view.createMeditation(RealDay)
    update_action = view.update(pageId)
    delete_action = view.delete(pageId)

else:
    list_scrp = os.listdir('copy_scripture/')
    if RealDay in list_scrp:
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        parser = view.parser()
        s = parser.find_all('p', {'class' : 'themeScrp'})
        scrip = s[0].text
        opened_list_scrp = open('copy_scripture/'+RealDay, 'w', encoding='UTF-8')
        opened_list_scrp.write(scrip)
        opened_list_scrp.close()
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()

    list_body = os.listdir('copy_bodytext/')
    if RealDay in list_body:
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        parser = view.parser()
        bt = parser.find_all('div', {'class' : 'bodyTxt'})
        body = bt[0].text
        opened_list_body = open('copy_bodytext/'+RealDay, 'w', encoding='UTF-8')
        opened_list_body.write(body)
        opened_list_body.close()
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()

    pageId = ''
    title = ''
    meditation = ''
    create_action = view.create(pageId)
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
 '''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, title_html=title, meditation_html=meditation, listStr_html=view.getDir(), create_action=create_action, update_action=update_action, delete_action=delete_action))
