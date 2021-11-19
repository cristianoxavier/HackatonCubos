from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/parceiros')
def parceiros():
    return render_template('parceiros.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')


if __name__ == '__main__':
    app.run()
