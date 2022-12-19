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


def Add_User():
    create_user = """
    INSERT INTO
      users (family, name, secname, date, phone)
    VALUES(?, ?, ?, ?, ?)"""
    return create_user










def Read_db():  # Функция чтения из DB
    with open('db.txt', 'r') as f:
        nums = f.read()
    return nums


def Add_db(x):  # Функция добавления в DB
    with open('db.txt', 'a') as f:
        f.write(f'\n {x}')


def Write_db(x):  # Функция перезаписи DB
    with open('db.txt', 'w') as f:
        f.write(f' {x}')


def Find_Atribut(name, db):  # Функция поиска в книжке, передаем DB и искомый атрибут
    for i in range(len(db)):
        if name in db[i]:
            print(f'Найден под номером {i} - {db[i].replace(";", " | ")}')



def Print_Record(numb, db):
    record = db[numb].split('; ')
    print(record)


def Edit_Atribut(numb, db):
    print(numb)
    record = db[numb - 1].split('; ')
    print(record)
    print(f'Сейчас - {record[numb - 1]}')
    record[numb - 1] = input("Введите изменения--> ")
    db[numb - 1] = str(record).replace("[", '')
    db[numb - 1] = db[numb - 1].replace(']', '')
    db[numb - 1] = db[numb - 1].replace("'", '')
    db[numb - 1] = db[numb - 1].replace(',', ';')
    db = str(db)
    db = db.replace('[', '')
    db = db.replace(']', '')
    db = db.replace(', ', '\n')
    db = db.replace("'", '')
    return (db)


def Del_Atribut(numb, db):
    db.remove(db[numb])
    db = str(db)
    db = db.replace('[', '')
    db = db.replace(']', '')
    db = db.replace(', ', '\n')
    db = db.replace("'", '')
    print("Удаление выполнено")
    return db


def To_CVS():
    with open('db.txt', 'r') as f:
        db = (f.read())
        list(db.split(';'))
        db.replace(';', ',')
        print(db)
    with open('db.csv', 'w') as f:
        writer = csv.writer(f, delimiter=' ', quotechar=' ', dialect='excel')
        writer.writerow(['Фамилия Имя Отчество;', 'Номер телефона;', 'Адрес проживани;'])
        writer.writerow(db)
    print("Конвертирование выполнено")
