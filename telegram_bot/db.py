import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from datetime import datetime

#---------------------------------------------ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ
def user_exist(user_id):
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
            try:
                date_time = result[-1].strip().split('-')
                date_time_now = str(datetime.now().date()).split('-')
                day = int(date_time[-1]) - int(date_time_now[-1])
                if day <= 0:
                    return True
                elif day > 0:
                    return False
            except:
                return False
    except Exception as ex:
        print(f'Error {ex}')
    finally:
        if connection:
            connection.close()

def user_add(user_id, pay=False):
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
                """UPDATE telegram_subs SET tg_id = {}, {}, {} WHERE tg_id = {};""".format(user_id, pay, datetime.now().date(), user_id)
            )
        return True
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()

def check_days_subs(user_id, date_mon):
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
            date = cursor.fetchone()[-1].strip()
            result = date_mon - date
    except Exception as ex:
        print(f'Error {ex}')
        return False
    finally:
        if connection:
            connection.close()

# print(user_exist('162092636'))
check_days_subs(162092696, '2021-12-23')