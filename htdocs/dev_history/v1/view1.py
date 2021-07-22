
import os, html_sanitizer

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
            <input type="submit" value="create">
        </form>
    '''.format(pageId)
    return create


def update(pageId):
    update = '''
        <form action="update.py?id={}" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="update">
        </form>
    '''.format(pageId, pageId)
    return update


def delete(pageId):
    delete = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
    return delete
