#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python.exe

print("Content-Type: text/html")
print()


import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
else:
    pageId = 'WWW(World Wide Web)'
    description = 'The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.'

print('''<!doctype html>
<html>
<head>
  <title>Lee's Family - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><strong><a href="index.py">Examining the Scriptures Daily</a><strong></h1>
  <ul>
    {listStr}
  </ul>

  <form action="process_update.py" method="post">
      <input type="hidden" name="pageId" value="{form_default_title}">
      <p><input type="text" name="title" placeholder="Title" value="{form_default_title}"></p>
      <p><textarea rows="10" name="description" placeholder="Description">{form_default_description}</textarea></p>
      <p><input type="submit" value="submit"></p>
  </form>
</body>
</html>
'''.format(listStr=view.getList(), form_default_title=title, form_default_description=description))
