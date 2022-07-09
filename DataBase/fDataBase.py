
class fDataBase():
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def AddUser(self, first_name, last_name, username,email_address, password,public_key, private_key):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM USERS WHERE EMAIL_ADDRESS LIKE '{email_address}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                return "Такой пользователь уже существует"

            self.__cur.execute("INSERT INTO USERS VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                               (first_name, last_name, username, email_address, password, public_key, private_key))
            self.__db.commit()
        except Exception as e:
            return "Ошибка в записи бд"

        return "Регистрация прошла успешно"

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM USERS WHERE ID = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                return False

            return res
        except Exception as e:
            print(f"Ошибка получения данных с бд{e}")

    def getUserInfo(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM USERS WHERE ID = '{user_id}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except Exception as e:
            print(f"Ошибка полученния данных из БД{e}")

        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM USERS WHERE EMAIL_ADDRESS = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except Exception as e:
            print(f"Ошибка получения данных из БД{e}")

        return False
