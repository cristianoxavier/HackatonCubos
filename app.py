from flask import Flask, render_template, request
from flask_mail import Mail

from controllers.buscar_controller import buscar_endereco

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pygmytectest@gmail.com'
app.config['MAIL_PASSWORD'] = 'l13J!$YmHHu1ACql'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/contato', methods=('GET', 'POST'))
def contato():
    if request.method == 'GET':
        return render_template('contato.html')
    if request.method == 'POST':
        args = request.form
        return envia_email(args)


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/parceiros', methods=('GET', 'POST'))
def parceiros():
    if request.method == 'GET':
        return render_template('parceiros.html')


@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'GET':
        return render_template('search.html')


@app.route('/signUp', methods=('GET', 'POST'))
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')
    elif request.method == 'POST':
        args = request.form
        return buscar_endereco(args)


if __name__ == '__main__':
    app.run()
