import ui
import action
import os
import sqlite3
from sqlite3 import Error
file_dir = os.path.dirname(os.path.realpath('__file__'))

def Start_PB():
    connection = action.create_connection()

    match (ui.Select_act()):
        case "1":
            book = action.Create_DB()
            action.execute_query(connection, book)
            connection.commit()
            connection.close()
        case "2":
            user = ui.Add_user()
            print(user)
            connection.execute("""INSERT INTO users (family, name, secname, date, phone) VALUES(?, ?, ?, ?, ?)""", user)
            connection.commit()

















            fio = ui.Input_PB()
            action.Add_db(fio)
        case "3":
            PB = list(action.Read_db().split('\n'))
            atribut = ui.Find_PB()
            action.Find_Atribut(atribut, PB)
        case "4":
            PB = list(action.Read_db().split('\n'))
            rec_num = ui.Edit_Rec()
            action.Print_Record(rec_num, PB)
            atribut = ui.Edit_Atribut()
            result = action.Edit_Atribut(atribut, PB)
            action.Write_db(result)
        case "5":
            PB = list(action.Read_db().split('\n'))
            numb = ui.Del_Rec()
            result = action.Del_Atribut(numb, PB)
            action.Write_db(result)
        case "5":
            action.To_CVS()
