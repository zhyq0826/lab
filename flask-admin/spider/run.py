from flask import (
    Flask, 
    request, 
    redirect, 
    url_for, 
    abort, 
    render_template, 
    flash
)


app = Flask(__name__, template_folder='templates', static_folder='static', static_path='/static')
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/task/new', methods=['POST', 'GET'])
def task_new():
    if request.method == 'GET':
        return render_template('task_new.html')
    else:
        return redirect(url_for('task'))


if __name__ == '__main__':
    app.run()