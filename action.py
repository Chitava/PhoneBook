import csv
import sqlite3
from sqlite3 import Error
import os
file_dir = os.path.dirname(os.path.realpath('__file__'))

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('PB.sqlite')
        print("Добро пожаловать в телефонную книгу")
    except Error as e:
        print(f"Произошла ошибка'{e}'")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Операция выполнена успешно")
    except Error as e:
        print(f"Возникла ошибка '{e}'")
        connection.close()

def Create_DB(): #Создание новой книги
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      family TEXT NOT NULL,
      name TEXT NOT NULL,
      secname TEXT NOT NULL,
      date TEXT,
      phone TEXT
    );
    """
    return create_users_table

def Add_user(connection, user):
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO users (family, name, secname, date, phone) VALUES (?, ?, ?, ?, ?)""", user)
        connection.commit()
        print("Операция выполнена успешно")
    except Error as e:
        print(f"Возникла ошибка '{e}'")
        connection.close()

def Find_user(connection, value, numb):
    match numb:
         case '1':
            cursor = connection.cursor()
            sql_select_query = """select * from users where family = ?;"""
            cursor.execute(sql_select_query, (value,))
            connection.commit()
            records = cursor.fetchall()
            for row in records:
                print("Фамилия:", row[1])
                print("Имя:", row[2])
                print("Отчество:", row[3])
                print("Дата рождения:", row[4])
                print("номер телефона:", row[5], end="\n\n")
            cursor.close()
         case '2':
            cursor = connection.cursor()
            sql_select_query = """select * from users where name = ?;"""
            cursor.execute(sql_select_query, (value,))
            connection.commit()
            records = cursor.fetchall()
            for row in records:
                print("Фамилия:", row[1])
                print("Имя:", row[2])
                print("Отчество:", row[3])
                print("Дата рождения:", row[4])
                print("номер телефона:", row[5], end="\n\n")
            cursor.close()
         case '3':
            cursor = connection.cursor()
            sql_select_query = """select * from users where secname = ?;"""
            cursor.execute(sql_select_query, (value,))
            connection.commit()
            records = cursor.fetchall()
            for row in records:
                print("Фамилия:", row[1])
                print("Имя:", row[2])
                print("Отчество:", row[3])
                print("Дата рождения:", row[4])
                print("номер телефона:", row[5], end="\n\n")
            cursor.close()
         case '4':
            cursor = connection.cursor()
            sql_select_query = """select * from users where date = ?;"""
            cursor.execute(sql_select_query, (value,))
            connection.commit()
            records = cursor.fetchall()
            for row in records:
                print("Фамилия:", row[1])
                print("Имя:", row[2])
                print("Отчество:", row[3])
                print("Дата рождения:", row[4])
                print("номер телефона:", row[5], end="\n\n")
            cursor.close()
         case '5':
            cursor = connection.cursor()
            sql_select_query = """select * from users where phone = ?;"""
            cursor.execute(sql_select_query, (value,))
            connection.commit()
            records = cursor.fetchall()
            for row in records:
                print("Фамилия:", row[1])
                print("Имя:", row[2])
                print("Отчество:", row[3])
                print("Дата рождения:", row[4])
                print("номер телефона:", row[5], end="\n\n")
            cursor.close()

def Del_rec(connection, numb):
    cursor = connection.cursor()

    def delet(numb):
        sql_select_query = """DELETE FROM users WHERE id = ?;"""
        cursor.execute(sql_select_query, numb)
        connection.commit()
        cursor.close

    if numb == "0":
        sql_select_query = """SELECT * from users;"""
        cursor.execute(sql_select_query)
        connection.commit()
        records = cursor.fetchall()
        for row in records:
            print("N:", row[0])
            print("Фамилия:", row[1])
            print("Имя:", row[2])
            print("Отчество:", row[3])
            print("Дата рождения:", row[4])
            print("номер телефона:", row[5], end="\n\n")
        cursor.close()
    numb = input("Введите номер записи которую нужно удалить")
    delet(numb)


def Logger(time, operation):
    with open('log.txt', 'a') as f:
        f.write(f'{time} произошла операция {operation}\n')


