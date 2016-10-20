#-*- encoding: utf-8 -*-

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

import pymysql
import pymysql.cursors


from werkzeug.contrib.fixers import ProxyFix



app = Flask(__name__, template_folder='templates', static_folder='static', static_path='/static')
app.config.from_object(__name__)
app.debug = True
app.config.update(dict(
    SECRET_KEY='test',
    USERNAME='admin',
    PASSWORD='admin'))


@app.route('/')
def index():
    return redirect(url_for('show_entries'))


@app.route('/blog')
def show_entries():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute('select * from entries')
        result = cursor.fetchall()

    print(result)
    return render_template('sql/index.html', result=result)


@app.route('/post', methods=['POST', 'GET'])
def post_entry():
    if request.method == 'GET':
        return render_template('sql/post.html')
    else:
        db = get_db()
        with db.cursor() as cursor:
            sql = 'insert into entries (title, `text`) values (%s, %s)'
            cursor.execute(sql, (request.form['title'], request.form['text']))
        db.commit()
        flash('new entry was successfully posted')
        return redirect(url_for('show_entries'))


def connect_db():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                             user='root',
                             charset='utf8mb4',
                             db='blog')

    
    return connection


def get_db():
    if not hasattr('g', 'mysqldb'):
        g.mysqldb = connect_db()

    return g.mysqldb


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mysqldb'):
        g.mysqldb.close()


# app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run()