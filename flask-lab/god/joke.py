#-*- coding: utf-8 -*-

import sys

print sys.getdefaultencoding() 

reload(sys)
sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding() 

from flask import (
    Flask,
    request,
    redirect,
    url_for,
    abort,
    session,
    g,
    render_template,
    flash
)


from werkzeug.contrib.fixers import ProxyFix


from db.conn import DBSession
from models.blog import Entries, User



app = Flask(__name__, template_folder='templates',
            static_folder='static', static_path='/static')
app.config.from_object(__name__)
app.debug = True
app.config.update(dict(
    SECRET_KEY='test',
    USERNAME='admin',
    PASSWORD='admin'))


@app.route('/')
def index():
    return redirect(url_for('show_entries'))


@app.route('/joke')
def show_entries():
    db = get_db()
    current_page = abs(int(request.args.get('page', 1)))
    result = db.query(Entries).offset((current_page-1)*10).limit(10)
    as_list = []
    for u in result:
        u.user = db.query(User).filter(User.id==u.uid).first()
        as_list.append(u)
    return render_template('joke/index.html', result=result, current_page=current_page)


def get_db():
    if not hasattr('g', 'mysqldb'):
        g.mysqldb = DBSession()

    return g.mysqldb


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mysqldb'):
        g.mysqldb.close()


if __name__ == '__main__':
    app.run(port=8000)
