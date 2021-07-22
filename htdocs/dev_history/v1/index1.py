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
    title = pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    create_action = ''
    update_action = view.update(pageId)
    delete_action = view.delete(pageId)
else:
    pageId = 'Daily Text'
    ti = soup.find_all('p', {'class' : 'themeScrp'})
    title = ti[0].text
    desc = soup.find_all('div', {'class' : 'bodyTxt'})
    description = desc[0].text
    create_action = view.create(pageId)
    update_action = ''
    delete_action = ''

print('''<!doctype html>
<html>
    <head>
      <title>Lee's Family - Welcome</title>
      <meta charset="utf-8">
    </head>

    <body>
      <h1><strong><a href="index.py">Examining the Scriptures Daily</a><strong></h1>
      <h2><strong>{today_html}</strong></h2>
      <h2><em>{title_html}</em></h2>
      <p>{description_html}</p>
      <ul>
        {listStr_html}
      </ul>
      {create_action}
      {update_action}
      {delete_action}
    </body>
</html>
 '''.format(title_html=title, description_html=description, listStr_html=view.getList(), create_action=create_action, update_action=update_action, delete_action=delete_action, today_html=RealDay))



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
