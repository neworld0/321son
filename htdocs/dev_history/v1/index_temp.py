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
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

form = cgi.FieldStorage()
day = datetime.today()
RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
sanitizer = html_sanitizer.Sanitizer()

if 'id' in form:
    pageId = form["id"].value
    s = soup.find_all('p', {'class' : 'themeScrp'})
    scripture = s[0].text
    bt = soup.find_all('div', {'class' : 'bodyTxt'})
    bodyText = bt[0].text
    m = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(pageId)
    meditation = sanitizer.sanitize(m)
    create_action = ''
    update_action = view.update(pageId)
    delete_action = view.delete(pageId)
else:
    pageId = 'Daily Text'
    s = soup.find_all('p', {'class' : 'themeScrp'})
    scripture = s[0].text
    bt = soup.find_all('div', {'class' : 'bodyTxt'})
    bodyText = bt[0].text
    DailyText = view.copyDailyText()
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
      <h2><font color ="#576cee"><em>{scripture_html}</em></font></h2>
      <p>{bodyText_html}</p>
      <h2><font color = "purple">{title_html}</font></h2>
      <p>{meditation_html}</p>
      <ul>
        <strong><font color = "red">
            {listStr_html}
        </font color></strong>
      </ul>
      {create_action}
      {update_action}
      {delete_action}
    </body>
</html>
 '''.format(today_html=RealDay, scripture_html=scripture, bodyText_html=bodyText, title_html=title, meditation_html=meditation, listStr_html=view.getList(), create_action=create_action, update_action=update_action, delete_action=delete_action))



# <div id="disqus_thread"></div>
# <script>
#
# /**
# # *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
# # *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
# /*
#
# var disqus_config = function () {
# this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
# this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
# };
# */
# (function() { // DON'T EDIT BELOW THIS LINE
# var d = document, s = d.createElement('script');
# s.src = 'https://web1-2.disqus.com/embed.js';
# s.setAttribute('data-timestamp', +new Date());
# (d.head || d.body).appendChild(s);
# })();
# </script>
# <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
