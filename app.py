import sqlite3
import os


from RSA.console_app import User as rsa_u
from DataBase import fDataBase
from flask import Flask, render_template, g, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from UserLogin import UserLogin


DATABASE = "databaseKAI.db"
SECRET_KEY = "QCQWCwfqw23r*7237^^23n2o3fqwc32"


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "databaseKAI.db")))


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Упс... 😖 Для начала вам надо зарегистрироваться'
login_manager.login_message_category = "danger"


dbase = None
user_rsa = None


@app.before_request
def before_request():
    global dbase
    global user_rsa
    db = get_db()
    dbase = fDataBase(db)
    user_rsa = rsa_u()

@login_manager.user_loader
def load_user(user_id):
    print("load user")
    return UserLogin().fromDB(user_id, dbase)


@app.route('/')
@app.route('/main_page', methods=['POST', 'GET'])
def main_page(): 
    return render_template('index.html', title="Главная страница")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        hash = generate_password_hash(password=request.form['Password'])
        public_user_key = user_rsa.public_key
        private_user_key = user_rsa.private_key
        result = dbase.AddUser(first_name=request.form['firstName'], last_name=request.form['lastName'],
                               email_address=request.form['email'], username=request.form['username'],
                               password=hash,
                               public_key=f"{public_user_key[0]};{public_user_key[1]}",
                               private_key=f"{private_user_key[0]};{private_user_key[1]}")
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
        if user and check_password_hash(user['PASSWORD'], request.form['psw']):
            userLogin = UserLogin().create(user)
            rememberMe = True if request.form.get('checkbox') else False
            login_user(userLogin, remember=rememberMe)
            return redirect(request.args.get('next') or url_for('main_page'))

        flash('Неверный логин или пароль',category="danger")
    return render_template('login.html', title="Авторизация")

@app.route('/Encrypt',  methods=['POST', 'GET'])
@login_required
def Encrypt():
    if request.method == "POST":
        answer = user_rsa.send_message(request.form['message'], [request.form['OneKey'], request.form['TwoKey']])
        return render_template("encrypt.html", title="Зашифровать сообщение",
                               us=dbase.getUserInfo(current_user.get_id()),
                               answer=f"{answer}")
    return render_template("encrypt.html", title="Зашифровать сообщение", us=dbase.getUserInfo(current_user.get_id()))


@app.route('/decipher',  methods=['POST', 'GET'])
@login_required
def decipher():
    if request.method == "POST":
        answer = user_rsa.show_message(request.form['message'], [request.form['OneKey'], request.form['TwoKey']])
        return render_template("decipher.html", title="Расшифровать сообщение",
                               us=dbase.getUserInfo(current_user.get_id()),
                               answer=answer)
    return render_template("decipher.html", title="Расшифровать сообщение", us=dbase.getUserInfo(current_user.get_id()))


@app.route('/profile',  methods=['POST', 'GET'])
@login_required
def profile():
    return f"user_info {current_user.get_id()}"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", category="success")
    return redirect(url_for("login"))

@app.errorhandler(404)
def error_404(error):
    return "Данная страница не найдена"


def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection


def get_db():
    """
    Данная функция устанавливает соединение с БД,
    если оно еще не установлено
    return:
    """
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """
    Данная функция закрывает соединение с БД,
    если оно не было установлено
    """
    if hasattr(g, 'link_db'):
        g.link_db.close()


def create_db():
    """
    Вспомогательная функция для создания таблиц в БД
    :return:
    """
    db = connect_db()
    with app.open_resource('databaseKAI_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


if __name__ == '__main__':
    app.run()
