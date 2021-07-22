import cgi, os, html_sanitizer, requests, sys
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

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


# def copyScripture(scrip):
#     day = datetime.today()
#     RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
#     target_folder = 'copy_scripture/'


# def copyText(body):
#     day = datetime.today()
#     RealDay = str(day.year)+'-'+str(day.month).zfill(2)+'-'+str(day.day).zfill(2)
#     target_folder = 'copy_bodytext/'


def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr


def create(pageId):
    create = '''
        <form action="create.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="생성">
        </form>
    '''.format(pageId)
    return create


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
