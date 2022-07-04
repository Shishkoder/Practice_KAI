from flask import Flask, render_template
from flask_login import LoginManager, login_user, login_required, current_user

DATABASE = "databaseKAI.db"
SECRET_KEY = "QCQWCwfqw23r*7237^^23n2o3fqwc32"


app = Flask(__name__)
app.config.from_object(__name__)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Упс... 😖 Для начала вам надо зарегистрироваться'
login_manager.login_message_category = "danger"


@app.route('/')
@app.route('/main_page')
def main_page(): 
    return render_template('index.html', title="Главная страница")



if __name__ == '__main__':
    app.run()
