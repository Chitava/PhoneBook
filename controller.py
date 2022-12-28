from action import *
import os
import datetime
import sqlite3
from sqlite3 import Error
import tkinter
import customtkinter
file_dir = os.path.dirname(os.path.realpath('__file__'))

def Start_PB():


    def All_rec():
        connect = create_connection()
        records = All(connect)
        frame_1 = customtkinter.CTkFrame(master=app)
        frame_1.place(x=5, y=5, width=470, height=370)
        result = customtkinter.CTkTextbox(master=frame_1, font=("Arial", 18))
        result.place(x=0, y=0, width=470, height=370)
        for row in records:
            result.insert("0.0", f"Запись N {row[1]}\nФамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\nДата рождения: {row[4]}\n"
                                 f"номер телефона: {row[5]}\n\n")

    def Find_rec():
        records = []
        def Finder():
            result = []
            item = fam.get()
            result.append(item)
            item = name.get()
            result.append(item)
            item = phon.get()
            result.append(item)
            connect = create_connection()
            records = Find_user(connect, result)
            if records == 'Записей нет':
                err('Записей нет')
            else:
                for row in records:
                    resul.insert("0.0", f"Запись N {row[0]}\nФамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\nДата рождения: {row[4]}\n"
                                        f"номер телефона: {row[5]}\n\n")
            records.clear()
            result.clear()
            find.destroy()
            return result

        find = customtkinter.CTk()
        find.geometry('470x200')
        find.title("Поиск в телефонном справочнике ")
        find.iconbitmap("img/Phonebook.ico")
        find.resizable(0, 0)
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
        frame_1 = customtkinter.CTkFrame(master=app)
        frame_1.place(x=5, y=5, width=470, height=390)
        resul = customtkinter.CTkTextbox(master=frame_1, font=("Arial", 18))
        resul.place(x=0, y=0, width=470, height=390)
        find.mainloop()

    def Add_rec():

        def Add():
            records = []
            item = family.get()
            records.append(item)
            item = name.get()
            records.append(item)
            item = secname.get()
            records.append(item)
            item = date.get()
            records.append(item)
            item = phone.get()
            records.append(item)
            connect = create_connection()
            Add_user(connect, records)
            records.clear()
            add.destroy()

        add = customtkinter.CTk()
        add.geometry('400x300')
        add.title("Создание новой записи ")
        add.iconbitmap("img/Phonebook.ico")
        add.resizable(0, 0)
        frame_f = customtkinter.CTkFrame(master=add)
        frame_f.place(x=5, y=5, width=390, height=290)
        family = customtkinter.CTkEntry(master=frame_f)
        family.grid(row=0, column=0, padx=10, pady=10)
        family_lab = customtkinter.CTkLabel(master=frame_f, text='фамилия', font=('Arial', 12), justify=tkinter.LEFT)
        family_lab.grid(row=0, column=1)
        name = customtkinter.CTkEntry(master=frame_f)
        name.grid(row=1, column=0)
        name_lab = customtkinter.CTkLabel(master=frame_f, text='Имя', font=('Arial', 12), justify=tkinter.LEFT)
        name_lab.grid(row=1, column=1)
        secname = customtkinter.CTkEntry(master=frame_f)
        secname.grid(row=2, column=0, padx=10, pady=10)
        secname_lab = customtkinter.CTkLabel(master=frame_f, text='отчество', font=('Arial', 12), justify=tkinter.LEFT)
        secname_lab.grid(row=2, column=1)
        date = customtkinter.CTkEntry(master=frame_f)
        date.grid(row=3, column=0)
        date_lab = customtkinter.CTkLabel(master=frame_f, text='дата рождения', font=('Arial', 12), justify=tkinter.LEFT)
        date_lab.grid(row=3, column=1)
        phone = customtkinter.CTkEntry(master=frame_f)
        phone.grid(row=4, column=0, padx=10, pady=10)
        phone_lab = customtkinter.CTkLabel(master=frame_f, text='телефон', font=('Arial', 12), justify=tkinter.LEFT)
        phone_lab.grid(row=4, column=1)
        quitButton = customtkinter.CTkButton(master=add, text="Добавить", command=Add)
        quitButton.place(x=225, y=230)
        frame_1 = customtkinter.CTkFrame(master=app)
        frame_1.place(x=5, y=5, width=470, height=390)
        resul = customtkinter.CTkTextbox(master=frame_1, font=("Arial", 18))
        resul.place(x=0, y=0, width=470, height=390)
        add.mainloop()







    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("600x400")
    app.title("Телефонная книга")
    app.iconbitmap("img/Phonebook.ico")
    app.resizable(0, 0)
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.place(x=5, y=5, width=470, height=390)
    frame_2 = customtkinter.CTkFrame(master=app)
    frame_2.place(x=490, y=5, width=115, height=390)
    button_1 = customtkinter.CTkButton(text='Найти', master=frame_2, command=Find_rec)
    button_1.pack(pady=5, padx=10)
    button_2 = customtkinter.CTkButton(text='Вывести всю', master=frame_2, command=All_rec)
    button_2.pack(pady=5, padx=10)
    button_3 = customtkinter.CTkButton(text='Добавить', master=frame_2, command=Add_rec)
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
    app.mainloop()