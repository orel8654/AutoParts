import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from datetime import datetime

#---------------------------------------------ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ НА НАХОЖДЕНИЕ В БАЗЕ
def user_id_check(user_id):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM telegram_subs WHERE tg_id = '{}'""".format(user_id)
            )
            result = cursor.fetchone()
            if result == None:
                return False
            else:
                return True
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()

#---------------------------------------------ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ, ПОСЛЕ ПЕРВОЙ ОПЛАТЫ
def user_add(user_id, pay=True):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO telegram_subs (tg_id, pay, date_time) VALUES ('{}', '{}', '{}');""".format(user_id, pay, datetime.now().date())
            )
        return True
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()

#---------------------------------------------ОБНОВЛЕНИЕ ЗАПИСИ ПОСЛЕ ОПЛАТЫ ПРОДЛЕНИЯ ПОДПИСКИ
def user_update(user_id, pay=True):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """UPDATE telegram_subs SET tg_id = {}, pay = {}, date_time = {} WHERE tg_id = {};""".format(user_id, pay, datetime.now().date(), user_id)
            )
        return True
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()

#---------------------------------------------ПРОВЕРКА ДНЕЙ ПОДПИСКИ, ПОДПИСКА ОФОРМЛЯЕТСЯ НА МЕСЯЦ
def check_days_subs(user_id):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT date_time FROM telegram_subs WHERE tg_id = {}""".format(user_id)
            )
            try:
                date = cursor.fetchone()[0].strip()
                result = datetime.now().date() - datetime.strptime(date, '%Y-%m-%d').date()
                result = str(result).split(' ')
                if int(result[0]) > 30:
                    return False
                else:
                    return True
            except ValueError as ex:
                return True
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()

#---------------------------------------------ДОБАВЛЕНИЕ АДМИНИСТРАТОРА
def admin_add(user_id, pay=True):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO telegram_subs (tg_id, pay, date_time) VALUES ('{}', '{}', '{}');""".format(user_id, 'Admin', datetime.now().date())
            )
        return True
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()