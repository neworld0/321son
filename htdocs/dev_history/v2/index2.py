#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

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
    m = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(pageId)
    meditation = sanitizer.sanitize(m)

    list_scrp = os.listdir('copy_scripture/')
    if not list_scrp:
        parser = view.parser()
        s = parser.find_all('p', {'class' : 'themeScrp'})
        scrip = s[0].text
        # view.copyScripture(scrip)
        opened_list_scrp = open('copy_scripture/'+RealDay, 'w', encoding='UTF-8')
        opened_list_scrp.write(scrip)
        opened_list_scrp.close()
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    elif list_scrp[0] != RealDay:
        for item in list_scrp:
            os.remove('copy_scripture/'+item)
        parser = view.parser()
        s = parser.find_all('p', {'class' : 'themeScrp'})
        scrip = s[0].text
        # view.copyScripture(scrip)
        opened_list_scrp = open('copy_scripture/'+RealDay, 'w', encoding='UTF-8')
        opened_list_scrp.write(scrip)
        opened_list_scrp.close()
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()

    list_body = os.listdir('copy_bodytext/')
    if not list_body:
        parser = view.parser()
        bt = parser.find_all('div', {'class' : 'bodyTxt'})
        body = bt[0].text
        # view.copyText(body)
        opened_list_body = open('copy_bodytext/'+RealDay, 'w', encoding='UTF-8')
        opened_list_body.write(body)
        opened_list_body.close()
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    elif list_body[0] != RealDay:
        for item in list_body:
            os.remove('copy_bodytext/'+item)
        parser = view.parser()
        bt = parser.find_all('div', {'class' : 'bodyTxt'})
        body = bt[0].text
        # view.copyText(body)
        opened_list_body = open('copy_bodytext/'+RealDay, 'w', encoding='UTF-8')
        opened_list_body.write(body)
        opened_list_body.close()
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()

    create_action = ''
    update_action = view.update(pageId)
    delete_action = view.delete(pageId)

else:
    list_scrp = os.listdir('copy_scripture/')
    if not list_scrp:
        parser = view.parser()
        s = parser.find_all('p', {'class' : 'themeScrp'})
        scrip = s[0].text
        # view.copyScripture(scrip)
        opened_list_scrp = open('copy_scripture/'+RealDay, 'w', encoding='UTF-8')
        opened_list_scrp.write(scrip)
        opened_list_scrp.close()
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    elif list_scrp[0] != RealDay:
        for item in list_scrp:
            os.remove('copy_scripture/'+item)
        parser = view.parser()
        s = parser.find_all('p', {'class' : 'themeScrp'})
        scrip = s[0].text
        # view.copyScripture(scrip)
        opened_list_scrp = open('copy_scripture/'+RealDay, 'w', encoding='UTF-8')
        opened_list_scrp.write(scrip)
        opened_list_scrp.close()
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()
    else:
        scripture = open('copy_scripture/'+RealDay, 'r', encoding='UTF-8').read()

    list_body = os.listdir('copy_bodytext/')
    if not list_body:
        parser = view.parser()
        bt = parser.find_all('div', {'class' : 'bodyTxt'})
        body = bt[0].text
        # view.copyText(body)
        opened_list_body = open('copy_bodytext/'+RealDay, 'w', encoding='UTF-8')
        opened_list_body.write(body)
        opened_list_body.close()
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    elif list_body[0] != RealDay:
        for item in list_body:
            os.remove('copy_bodytext/'+item)
        parser = view.parser()
        bt = parser.find_all('div', {'class' : 'bodyTxt'})
        body = bt[0].text
        # view.copyText(body)
        opened_list_body = open('copy_bodytext/'+RealDay, 'w', encoding='UTF-8')
        opened_list_body.write(body)
        opened_list_body.close()
        bodyText = open('copy_bodytext/'+RealDay, 'r', encoding='UTF-8').read()
    else:
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
    </head>
    <body>
      <h1><strong><a href="index.py">Examining the Scriptures Daily</a></strong></h1>
      <h2><strong>{today_html}</strong></h2>
      <h2><font color="blue"><em>{scripture_html}</em></font></h2>
      <p>{bodyText_html}</p>
      <h2>{title_html}</h2>
      <p>{meditation_html}</p>
      <ul>
        <strong>
            {listStr_html}
        </strong>
      </ul>
      {create_action}
      {update_action}
      {delete_action}
    </body>
</html>
 '''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, title_html=title, meditation_html=meditation, listStr_html=view.getList(), create_action=create_action, update_action=update_action, delete_action=delete_action))
