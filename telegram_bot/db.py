import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from datetime import datetime
import sqlite3


'''ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ В БАЗЕ'''
def user_id_check(user_id):
    connection = sqlite3.connect('db_telegram.db')
    cursor = connection.cursor()

    with connection:
        result = cursor.execute("SELECT * FROM telegram_subs WHERE tg_id = ?", (user_id,)).fetchall()
        return bool(len(result))

'''ДОБАВЛЕНИЕ ПОСЛЕ ОПЛАТЫ'''
def user_add(user_id, pay='True'):
    connection = sqlite3.connect('db_telegram.db')
    cursor = connection.cursor()

    data_tuple = (user_id, pay, datetime.now().date())
    with connection:
        try:
            result = "INSERT INTO telegram_subs (tg_id, pay, date) VALUES (?, ?, ?);"
            cursor.execute(result, data_tuple)
            connection.commit()
            return True
        except:
            return False

'''ОБНОВЛЕНИЕ ПОСЛЕ ПРОДЛЕНИЯ ПОДПИСКИ'''
def user_update(user_id, pay='True'):
    connection = sqlite3.connect('db_telegram.db')
    cursor = connection.cursor()

    data_tuple = (user_id, pay, datetime.now().date(), user_id)
    with connection:
        try:
            result = "UPDATE telegram_subs SET tg_id = ?, pay = ?, date = ? WHERE tg_id = ?;"
            cursor.execute(result, data_tuple)
            connection.commit()
            return True
        except:
            return False

'''ПРОВЕРКА ДНЕЙ ПОДПИСКИ'''
def check_days_subs(user_id):
    connection = sqlite3.connect('db_telegram.db')
    cursor = connection.cursor()

    with connection:
        date = cursor.execute("SELECT date FROM telegram_subs WHERE tg_id = ?", (user_id,)).fetchone()[0].strip()
        try:
            result = datetime.now().date() - datetime.strptime(date, '%Y-%m-%d').date()
            result = str(result).split(' ')
            if int(result[0]) > 30:
                return False
            else:
                return True
        except ValueError:
            return True

'''ДОБАВЛЕНИЕ АДМИНИМТРАТОРА'''
def admin_add(user_id, pay='True'):
    connection = sqlite3.connect('db_telegram.db')
    cursor = connection.cursor()
    data_tuple = (user_id, 'Admin', datetime.now().date())
    with connection:
        try:
            result = "INSERT INTO telegram_subs (tg_id, pay, date) VALUES (?, ?, ?);"
            cursor.execute(result, data_tuple)
            connection.commit()
            return True
        except:
            return False








# #---------------------------------------------ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ НА НАХОЖДЕНИЕ В БАЗЕ
# def user_id_check(user_id):
#     try:
#         connection = psycopg2.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME,
#         )
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """SELECT * FROM telegram_subs WHERE tg_id = '{}'""".format(user_id)
#             )
#             result = cursor.fetchone()
#             if result == None:
#                 return False
#             else:
#                 return True
#     except Exception as ex:
#         print(f'Error {ex}')
#         return False
#     finally:
#         if connection:
#             connection.close()
#
# #---------------------------------------------ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ, ПОСЛЕ ПЕРВОЙ ОПЛАТЫ
# def user_add(user_id, pay=True):
#     try:
#         connection = psycopg2.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME,
#         )
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """INSERT INTO telegram_subs (tg_id, pay, date_time) VALUES ('{}', '{}', '{}');""".format(user_id, pay, datetime.now().date())
#             )
#         return True
#     except Exception as ex:
#         print(f'Error {ex}')
#         return False
#     finally:
#         if connection:
#             connection.close()
#
# #---------------------------------------------ОБНОВЛЕНИЕ ЗАПИСИ ПОСЛЕ ОПЛАТЫ ПРОДЛЕНИЯ ПОДПИСКИ
# def user_update(user_id, pay=True):
#     try:
#         connection = psycopg2.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME,
#         )
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """UPDATE telegram_subs SET tg_id = {}, pay = {}, date_time = {} WHERE tg_id = {};""".format(user_id, pay, datetime.now().date(), user_id)
#             )
#         return True
#     except Exception as ex:
#         print(f'Error {ex}')
#         return False
#     finally:
#         if connection:
#             connection.close()
#
# #---------------------------------------------ПРОВЕРКА ДНЕЙ ПОДПИСКИ, ПОДПИСКА ОФОРМЛЯЕТСЯ НА МЕСЯЦ
# def check_days_subs(user_id):
#     try:
#         connection = psycopg2.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME,
#         )
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """SELECT date_time FROM telegram_subs WHERE tg_id = {}""".format(user_id)
#             )
#             try:
#                 date = cursor.fetchone()[0].strip()
#                 result = datetime.now().date() - datetime.strptime(date, '%Y-%m-%d').date()
#                 result = str(result).split(' ')
#                 if int(result[0]) > 30:
#                     return False
#                 else:
#                     return True
#             except ValueError as ex:
#                 return True
#     except Exception as ex:
#         print(f'Error {ex}')
#         return False
#     finally:
#         if connection:
#             connection.close()
#
# #---------------------------------------------ДОБАВЛЕНИЕ АДМИНИСТРАТОРА
# def admin_add(user_id, pay=True):
#     try:
#         connection = psycopg2.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME,
#         )
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """INSERT INTO telegram_subs (tg_id, pay, date_time) VALUES ('{}', '{}', '{}');""".format(user_id, 'Admin', datetime.now().date())
#             )
#         return True
#     except Exception as ex:
#         print(f'Error {ex}')
#         return False
#     finally:
#         if connection:
#             connection.close()


# if __name__ == '__main__':
#     print(user_id_check('162092696'))