import os
import sqlite3
from sqlite3 import Error

from controller import *
import tkinter
import customtkinter
file_dir = os.path.dirname(os.path.realpath('__file__'))


def err(text): #Сообщение об ошибках
    error = customtkinter.CTk()
    error.geometry("300x200")
    error.title("Возникла ошибка")
    error.iconbitmap("img/Phonebook.ico")
    error.resizable(0, 0)
    frame_er = customtkinter.CTkFrame(master=error)
    frame_er.place(x=5, y=5, width=290, height=190)
    label_100 = customtkinter.CTkLabel(master=frame_er, text=text, font=('Arial', 10), justify=tkinter.LEFT)
    label_100.pack(pady=50, padx=10)
    quitButton = customtkinter.CTkButton(master=frame_er, text="Закрыть", command=error.destroy)
    quitButton.pack(pady=10, padx=10)
    error.mainloop()


def done(): #Сообщение об успешной операции
    error = customtkinter.CTk()
    error.geometry("300x200")
    error.title("Операция завершениа ")
    error.iconbitmap("img/Phonebook.ico")
    error.resizable(0, 0)
    frame_er = customtkinter.CTkFrame(master=error)
    frame_er.place(x=5, y=5, width=290, height=190)
    label_100 = customtkinter.CTkLabel(master=frame_er, text='Операция выполнена успешно!', font=('Arial', 18), justify=tkinter.LEFT)
    label_100.pack(pady=50, padx=10)
    quitButton = customtkinter.CTkButton(master=frame_er, text="Закрыть", command=error.destroy)
    quitButton.pack(pady=10, padx=10)
    error.mainloop()


def save(optionmenu_1): # нажатие кнопки сохранить в....
    print(optionmenu_1)


def create_connection():#Соединение с SQL
    connection = None
    try:
        connection = sqlite3.connect('DB/PB.sqlite')
    except Error as e:
        err(f"Произошла ошибка'{e}'")
    return connection


def execute_query(connection, query): #Выполнить запрос SQL
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        done()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()


def Add_user(connection, user): #Добавление нового пользователя
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO users (family, name, secname, date, phone) VALUES (?, ?, ?, ?, ?)""", user)
        connection.commit()
        done()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()


def All(connection): #Вывод всей книги
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM users""" )
        connection.commit()
        records = cursor.fetchall()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()
    return records


def Delet(connection, numb):# Удаление записей
    cursor = connection.cursor()
    sql_select_query = """DELETE FROM users WHERE id = ?;"""
    try:
        cursor.execute(sql_select_query, numb)
        connection.commit()
        done()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()

    cursor.close


def Logger(time, operation): #Логирование
    with open('log.txt', 'a') as f:
        f.write(f'{time} произошла операция {operation}\n')



def Find_user(connection, value): #Поиск записей
    if (value[1] == '' and value[2] == ''):
        sql_select_query = """select * from users where family=?"""
        records = Connect_one(connection, sql_select_query, value[0])
    elif (value[0] == '' and value[2] == ''):
        sql_select_query = """select * from users where name = ?;"""
        records = Connect_one(connection, sql_select_query, value[1])
    elif (value[0] == '' and value[1] == ''):
        sql_select_query = """select * from users where phone = ?;"""
        records = Connect_one(connection, sql_select_query, value[2])
    elif (value[2] == ''):
        value.remove('')
        sql_select_query = """select * from users where family = ? and name = ?;"""
        records = Connect_many(connection, sql_select_query, value)
    elif (value[1] == ''):
        value.remove('')
        sql_select_query = """select * from users where family = ? and phone = ?;"""
        records = Connect_many(connection, sql_select_query, value)
    elif (value[0]) == '':
        value.remove('')
        sql_select_query = """select * from users where name = ? and phone = ?;"""
        records = Connect_many(connection, sql_select_query, value)
    else:
        sql_select_query = """select * from users where family = ? and name = ? and phone = ?;"""
        records = Connect_many(connection, sql_select_query, value)
    return records


def Connect_one(connection, sql_select_query, value): #Соединение с базой SQL когда поиск происходит по 1 параметру
    cursor = connection.cursor()
    cursor.execute(sql_select_query, (value,))
    connection.commit()
    records = cursor.fetchall()
    if not records:
        records = 'Записей нет'
    cursor.close()
    return records


def Connect_many(connection, sql_select_query, value):#Соединение с базой SQL когда поиск происходит по нескольким парам.
    cursor = connection.cursor()
    cursor.execute(sql_select_query, value)
    connection.commit()
    records = cursor.fetchall()
    if not records:
        records = 'Записей нет'
    cursor.close()
    return records


def Chenge(connection, numb):
    cursor = connection.cursor()
    sql_select_query = """select * from users where id = ?;"""
    try:
        cursor.execute(sql_select_query, numb)
        connection.commit()
        records = cursor.fetchall()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()
    cursor.close
    return records


def Exchenge(data, name):
    print(data)
    connection = create_connection()
    cursor = connection.cursor()
    sqlite_update_query = """UPDATE users SET family = ?, name = ?, secname = ?, date = ?, phone = ? WHERE id = ?;"""
    try:
        cursor.execute(sqlite_update_query, data)
        connection.commit()
        name.destroy()
        done()
    except Error as e:
        print(e)
        err(f"Произошла ошибка'{e}'")

        connection.close()
    cursor.close














