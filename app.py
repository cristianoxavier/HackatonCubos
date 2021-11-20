from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail
from configurations.enviroment import EMAIL, EMAIL_PASSWORD

from controllers.buscar_controller import buscar_endereco
from controllers.contato_controller import envia_email

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
        msg = envia_email(args)
        if msg == "":
            error = 'Erro ao Enviar email'
        else:
            mail.send(msg)
            flash("Email enviado com sucesso")
            return redirect(url_for('contato'))
    return render_template('contato.html', error=error)


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
        map = buscar_endereco({'localizacao': 'brasil'})
        return render_template('search.html', map=map._repr_html_())
    elif request.method == "POST":
        args = request.form
        map = buscar_endereco(args)
        return render_template('search.html', map=map._repr_html_())


@app.route('/signUp', methods=('GET', 'POST'))
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')
    elif request.method == 'POST':
        args = request.form
        return buscar_endereco(args)


if __name__ == '__main__':
    app.run()
