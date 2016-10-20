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

from werkzeug.contrib.fixers import ProxyFix


from db.conn import DBSession
from models.blog import Entries


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


@app.route('/blog')
def show_entries():
    db = get_db()
    result = db.query(Entries)
    return render_template('alchemy/index.html', result=result)


@app.route('/post', methods=['POST', 'GET'])
def post_entry():
    if request.method == 'GET':
        return render_template('alchemy/post.html')
    else:
        db = get_db()
        db.add(Entries(title=request.form['title'], text=request.form['text']))
        db.commit()
        flash('new entry was successfully posted')
        return redirect(url_for('show_entries'))
@app.route('/post/<int:post_id>')
def post(post_id):
    db = get_db()
    entry = db.query(Entries).filter(Entries.id==post_id).one()
    if not entry:
        abort(404)
    return render_template('alchemy/detail.html', post=entry)



def get_db():
    if not hasattr('g', 'mysqldb'):
        g.mysqldb = DBSession()

    return g.mysqldb


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mysqldb'):
        g.mysqldb.close()


if __name__ == '__main__':
    app.run()
