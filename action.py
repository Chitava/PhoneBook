import csv
import sqlite3
from sqlite3 import Error
import os
from controller import *
import tkinter
import customtkinter
file_dir = os.path.dirname(os.path.realpath('__file__'))


def err(text):
    error = customtkinter.CTk()
    error.geometry("300x200")
    error.title("Возникла ошибка")
    error.iconbitmap("img/Phonebook.ico")
    frame_er = customtkinter.CTkFrame(master=error)
    frame_er.place(x=5, y=5, width=290, height=190)
    label_100 = customtkinter.CTkLabel(master=frame_er, text=text, font=('Arial', 14), justify=tkinter.LEFT)
    label_100.pack(pady=50, padx=10)
    quitButton = customtkinter.CTkButton(master=frame_er, text="Закрыть", command=error.destroy)
    quitButton.pack(pady=10, padx=10)
    error.mainloop()


def done():
    error = customtkinter.CTk()
    error.geometry("300x200")
    error.title("Операция завершениа ")
    error.iconbitmap("img/Phonebook.ico")
    frame_er = customtkinter.CTkFrame(master=error)
    frame_er.place(x=5, y=5, width=290, height=190)
    label_100 = customtkinter.CTkLabel(master=frame_er, text='Операция выполнена успешно!', font=('Arial', 18), justify=tkinter.LEFT)
    label_100.pack(pady=50, padx=10)
    quitButton = customtkinter.CTkButton(master=frame_er, text="Закрыть", command=error.destroy)
    quitButton.pack(pady=10, padx=10)
    error.mainloop()


def find():
    result = []
    def Finder():
        item = fam.get()
        result.append(item)
        item = name.get()
        result.append(item)
        item = phon.get()
        result.append(item)
        connect=create_connection()






        find.destroy()
        print(result)
        return result









    find = customtkinter.CTk()
    find.geometry('470x200')
    find.title("Поиск в телефонном справочнике ")
    find.iconbitmap("img/Phonebook.ico")
    frame_f = customtkinter.CTkFrame(master=find)
    frame_f.place(x=5, y=5, width=460, height=192)
    fam = customtkinter.CTkEntry(master=frame_f)
    fam.grid(row=0, column=0)
    family_lab = customtkinter.CTkLabel(master=frame_f, text='фамилия', font=('Arial', 12), justify=tkinter.LEFT)
    family_lab.place(x=45, y=53)
    name = customtkinter.CTkEntry(master=frame_f)
    name.grid(row=0, column=1, padx=20, pady=15)
    name_lab = customtkinter.CTkLabel(master=frame_f, text='Имя', font=('Arial', 12), justify=tkinter.LEFT)
    name_lab.place(x=220, y=53)
    phon = customtkinter.CTkEntry(master=frame_f)
    phon.grid(row=0, column=2)
    phon_lab = customtkinter.CTkLabel(master=frame_f, text='телефон', font=('Arial', 12), justify=tkinter.LEFT)
    phon_lab.place(x=365, y=53)
    quitButton = customtkinter.CTkButton(master=find, text="Поиск", command=Finder)
    quitButton.place(x=325, y=150)











    find.mainloop()










def save(optionmenu_1): # нажатие кнопки сохранить в....
    print(optionmenu_1)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('DB/PB.sqlite')
    except Error as e:
        err(f"Произошла ошибка'{e}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        done()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()


def Add_user(connection, user):
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO users (family, name, secname, date, phone) VALUES (?, ?, ?, ?, ?)""", user)
        connection.commit()
        done()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()


def All(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM users""" )
        connection.commit()
        records = cursor.fetchall()
    except Error as e:
        err(f"Произошла ошибка'{e}'")
        connection.close()
    return records


def Find_user(connection, value, numb):
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


