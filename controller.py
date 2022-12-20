import ui
import action
import os
import datetime
import sqlite3
from sqlite3 import Error
file_dir = os.path.dirname(os.path.realpath('__file__'))

def Start_PB():
    match (ui.Select_act()):
        case "1":
            connection = action.create_connection()
            query = action.Create_DB()
            action.execute_query(connection, query)
            action.Logger(datetime.date.today(), 'создание новой телефонной книги')


        case "2":
            connection = action.create_connection()
            user = list(ui.Add_user())
            action.Add_user(connection, user)
            action.Logger(datetime.date.today(), 'добавление нового пользователя')

        case "3":
            connection = action.create_connection()
            act = ui.Select_find()
            action.Find_user(connection, act[0], act[1])
            action.Logger(datetime.date.today(), 'поиск пользователя')

        case "4":
            connection = action.create_connection()
            numb = ui.Del_rec()
            action.Del_rec(connection, numb)
            action.Logger(datetime.date.today(), 'удаление пользователя')
















