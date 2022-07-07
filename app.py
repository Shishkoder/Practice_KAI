import sqlite3
import os


from DataBase import fDataBase
from flask import Flask, render_template, g, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from UserLogin import UserLogin

DATABASE = "databaseKAI.db"
SECRET_KEY = "QCQWCwfqw23r*7237^^23n2o3fqwc32"
dbase = None


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "databaseKAI.db")))


# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message = 'Упс... 😖 Для начала вам надо зарегистрироваться'
# login_manager.login_message_category = "danger"


@app.route('/')
@app.route('/main_page', methods=['POST', 'GET'])
def main_page(): 
    return render_template('index.html', title="Главная страница")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        hash = generate_password_hash(password=request.form['Password'])
        result = dbase.AddUser(first_name=request.form['firstName'], last_name=request.form['lastName'],
                               email_address=request.form['email'], username=request.form['username'],
                               password=hash, public_key=1, private_key=1)
        if result == "Такой пользователь уже существует":
            flash("Такой пользователь уже существует",category="danger")
        elif result == "Ошибка в записи бд":
            flash("Ошибка создания аккаунта", category="danger")
        else:
            return redirect(url_for('main_page'))
    return render_template('register.html', title="Регистрация нового пользователя")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        # if user and check_password_hash()
    return render_template('login.html', title=Авторизация)


@app.route('/profile')
@login_required
def profile():
    return "Профиль"


@app.errorhandler(404)
def error_404(error):
    return "Данная страница не найдена"


@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = fDataBase(db)


def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


def create_db():
    db = connect_db()
    with app.open_resource('databaseKAI_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


if __name__ == '__main__':
    app.run()
