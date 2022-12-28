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


#########################################################
def Find():
    def Finder():
        result = []
        item = fam.get()
        result.append(item)
        item = name.get()
        result.append(item)
        item = phon.get()
        result.append(item)
        connect = create_connection()
        result = Find_user(connect, result)
        find.destroy()
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        app = customtkinter.CTk()
        app.geometry("600x400")
        app.title("Телефонная книга")
        app.iconbitmap("img/Phonebook.ico")
        frame_1 = customtkinter.CTkFrame(master=app)
        frame_1.place(x=5, y=5, width=470, height=390)
        frame_2 = customtkinter.CTkFrame(master=app)
        frame_2.place(x=490, y=5, width=115, height=390)
        button_1 = customtkinter.CTkButton(text='Найти', master=frame_2, command=Find)
        button_1.pack(pady=5, padx=10)
        button_2 = customtkinter.CTkButton(text='Вывести всю', master=frame_2, command=All_rec)
        button_2.pack(pady=5, padx=10)
        button_3 = customtkinter.CTkButton(text='Добавить', master=frame_2)
        button_3.pack(pady=5, padx=10)
        button_3 = customtkinter.CTkButton(text='Изменить', master=frame_2)
        button_3.pack(pady=5, padx=10)
        button_3 = customtkinter.CTkButton(text='Удалить', master=frame_2)
        button_3.pack(pady=5, padx=10)
        label_save = customtkinter.CTkLabel(text='Сохранить в', master=frame_2, justify=tkinter.LEFT)
        label_save.pack(pady=5, padx=10)
        optionmenu_1 = customtkinter.CTkOptionMenu(frame_2, values=["CVS", "EXCEL", "TXT"], command=save)
        optionmenu_1.pack(pady=10, padx=10)
        optionmenu_1.set("формат")
        label_100 = customtkinter.CTkLabel(text='', master=frame_2, justify=tkinter.LEFT)
        label_100.pack(pady=5, padx=10)
        label_i = customtkinter.CTkLabel(text='ООО "Инстэл"', master=frame_2, justify=tkinter.LEFT)
        label_i.pack(pady=5, padx=10)
        label_e = customtkinter.CTkLabel(text='2022 г.', master=frame_2, justify=tkinter.LEFT)
        label_e.pack(padx=10)
        label_1 = customtkinter.CTkLabel(text='Ваша телефонная книжка', master=frame_1, justify=tkinter.LEFT,
                                         font=('Arial', 35, 'italic'), )
        label_1.pack(padx=10)
        label_1 = customtkinter.CTkLabel(text='Выберете действие в меню справа', master=frame_1, justify=tkinter.LEFT,
                                         font=('Arial', 20, 'italic'))
        label_1.pack(padx=10, pady=100)
        frame_1 = customtkinter.CTkFrame(master=app)
        frame_1.place(x=5, y=5, width=470, height=370)
        resul = customtkinter.CTkTextbox(master=frame_1, font=("Arial", 18))
        resul.place(x=0, y=0, width=470, height=370)
        for row in result:
            resul.insert("0.0", f"Фамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\nДата рождения: {row[4]}\n"
                                 f"номер телефона: {row[5]}\n\n")


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




def Find_user(connection, value):
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


def Connect_one(connection, sql_select_query, value):
    cursor = connection.cursor()
    cursor.execute(sql_select_query, (value,))
    connection.commit()
    records = cursor.fetchall()
    if not records:
        records = 'Записей нет'
    cursor.close()
    return records


def Connect_many(connection, sql_select_query, value):
    cursor = connection.cursor()
    cursor.execute(sql_select_query, value)
    connection.commit()
    records = cursor.fetchall()
    if not records:
        records = 'Записей нет'
    cursor.close()
    return records

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





def All_rec():
    connect = create_connection()
    records = All(connect)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("600x400")
    app.title("Телефонная книга")
    app.iconbitmap("img/Phonebook.ico")
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.place(x=5, y=5, width=470, height=390)
    frame_2 = customtkinter.CTkFrame(master=app)
    frame_2.place(x=490, y=5, width=115, height=390)
    button_1 = customtkinter.CTkButton(text='Найти', master=frame_2, command=Find)
    button_1.pack(pady=5, padx=10)
    button_2 = customtkinter.CTkButton(text='Вывести всю', master=frame_2, command=All_rec)
    button_2.pack(pady=5, padx=10)
    button_3 = customtkinter.CTkButton(text='Добавить', master=frame_2)
    button_3.pack(pady=5, padx=10)
    button_3 = customtkinter.CTkButton(text='Изменить', master=frame_2)
    button_3.pack(pady=5, padx=10)
    button_3 = customtkinter.CTkButton(text='Удалить', master=frame_2)
    button_3.pack(pady=5, padx=10)
    label_save = customtkinter.CTkLabel(text='Сохранить в', master=frame_2, justify=tkinter.LEFT)
    label_save.pack(pady=5, padx=10)
    optionmenu_1 = customtkinter.CTkOptionMenu(frame_2, values=["CVS", "EXCEL", "TXT"], command=save)
    optionmenu_1.pack(pady=10, padx=10)
    optionmenu_1.set("формат")
    label_100 = customtkinter.CTkLabel(text='', master=frame_2, justify=tkinter.LEFT)
    label_100.pack(pady=5, padx=10)
    label_i = customtkinter.CTkLabel(text='ООО "Инстэл"', master=frame_2, justify=tkinter.LEFT)
    label_i.pack(pady=5, padx=10)
    label_e = customtkinter.CTkLabel(text='2022 г.', master=frame_2, justify=tkinter.LEFT)
    label_e.pack(padx=10)
    label_1 = customtkinter.CTkLabel(text='Ваша телефонная книжка', master=frame_1, justify=tkinter.LEFT,
                                     font=('Arial', 35, 'italic'), )
    label_1.pack(padx=10)
    label_1 = customtkinter.CTkLabel(text='Выберете действие в меню справа', master=frame_1, justify=tkinter.LEFT,
                                     font=('Arial', 20, 'italic'))
    label_1.pack(padx=10, pady=100)
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.place(x=5, y=5, width=470, height=370)
    result = customtkinter.CTkTextbox(master=frame_1, font=("Arial", 18))
    result.place(x=0, y=0, width=470, height=370)
    for row in records:
        result.insert("0.0", f"Фамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\nДата рождения: {row[4]}\n"
                                 f"номер телефона: {row[5]}\n\n")
    app.mainloop()










