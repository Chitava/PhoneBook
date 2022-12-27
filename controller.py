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
            result.insert("0.0", f"Фамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\nДата рождения: {row[4]}\n"
                                 f"номер телефона: {row[5]}\n\n")



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
    button_1 = customtkinter.CTkButton(text='Найти', master=frame_2, command=find)
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
    app.mainloop()