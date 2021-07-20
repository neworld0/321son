import cgi, os, html_sanitizer, requests, sys, glob
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def getDir():
    root = 'data'
    dirStr = ''
    with os.scandir(root) as entries:
        for entry in entries:
            if entry.is_dir():
                dirStr = dirStr + '<li><a href="meditation.py?id={directory}">{directory}</a></li>'.format(directory=entry.name)
    return dirStr

def getDateList():
    sanitizer = html_sanitizer.Sanitizer()
    form = cgi.FieldStorage()
    Id = form["id"].value       # Id = 'Jeonghun\'s_Meditation/2021-07-13'
    pageId = Id[:-10]
    root = 'data/'+pageId+'*'
    files = glob.glob(root)
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        i = item[5:]
        link = i.replace("\\", "/")
        list = link[-10:]
        listStr = listStr + '<li><a href="personal_meditation_list.py?id={page}">{name}</a></li>'.format(page=link, name=list)
    return listStr

def getPersonalList():
    sanitizer = html_sanitizer.Sanitizer()
    form = cgi.FieldStorage()
    pageId = form["id"].value
    root = 'data/'+pageId
    files = os.listdir(root)
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="personal_meditation_list.py?id={name}/{file}">{file}</a></li>'.format(name=pageId, file=item)
    return listStr

def getMeditationList():
    sanitizer = html_sanitizer.Sanitizer()
    root = 'data/'
    files = os.listdir(root)
    print(files)
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="personal_meditation_list.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr

def getMeditation():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="meditation.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr

def parser():
    t = datetime.today()+timedelta(1)
    y = str(t.year)
    m = str(t.month).zfill(2)
    d = str(t.day).zfill(2)
    today = y+'/'+m+'/'+d
    url = 'https://wol.jw.org/ko/wol/h/r8/lp-ko/'+ today
    r = requests.get(url)
    parser = BeautifulSoup(r.text, 'html.parser')
    return parser

def create(pageId):
    create = '''
        <form action="create.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="이름 생성">
        </form>
    '''.format(pageId)
    return create

def createMeditation(pageId):
    createMeditation = '''
        <form action="create_meditation.py?={}" method="post">
            <input type="hidden" name="your_name" value="{}">
            <input type="submit" value="묵상 기록">
        </form>
    '''.format(pageId, pageId)
    return createMeditation

def update(pageId):
    update = '''
        <form action="update.py?id={}" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="수정">
        </form>
    '''.format(pageId, pageId)
    return update

def delete(pageId):
    delete = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="삭제">
        </form>
    '''.format(pageId)
    return delete
