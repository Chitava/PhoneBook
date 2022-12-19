import action


# Выбор действия с DB
def Select_act():
    print("Что Вы хотите сделать в телефонной книге")
    print("1 - Создать новую книжку")
    print("2 - Создать новую запись")
    print("3 - Найти запись о человеке")
    print("4 - Редактировать запись")
    print("5 - Удалить запись")
    act = input("Выберите действие --> ")
    temp = False
    while temp == False:
        if act == '1' or act == '2' or act == '3' or act == '4' or act == '5':
            temp = True
        else:
            act = input("Не верный выбор, введите цифру от 1 до 5 --> ")
    return act


def Add_user():
    user = []
    family = input('Введите фамилию ')
    user.append(family)
    name = input('Введите имя ')
    user.append(name)
    secname = input('Введите отчество ')
    user.append(secname)
    date = input('Введите дату рождения ')
    user.append(date)
    phone = input('Введите номер телефона ')
    user.append(phone)
    return user





# Ввод ФИО в DB
def Input_PB():
    line = ('')
    line += (input("Введите фамилию --> "))
    line += ' ' + input("Введите имя --> ")
    line += ' ' + input("Введите отчество --> ") + ";"
    line += ' ' + input("Введите телефон --> ") + ";"
    line += ' ' + input("Введите адрес --> ")
    return line


# Поиск по DB
def Find_PB():
    return input("Введите что будем искать: Фамилию либо имя либо телефон либо адрес --> ")


# Редактирование записей
def Edit_Rec():
    return int(input("Введите номер записи --> "))


# Выбор редактирования
def Edit_Atribut():
    print('1 - редактировать ФИО')
    print('2 - редактировать телефон')
    print('3 - редактировать адрес')
    act = input("Введите число --> ")
    temp = False
    while temp == False:
        if act == '1' or act == '2' or act == '3':
            temp = True
        else:
            act = (input("Не верный выбор, введите цифру от 1 до 3 --> "))
        return int(act)


def Del_Rec():
    return int(input("Введите номер записи --> "))
