import action


# Выбор действия с DB
def Select_act():
    print("Что Вы хотите сделать в телефонной книге")
    print("1 - Создать новую книжку")
    print("2 - Создать новую запись")
    print("3 - Найти запись о человеке")
    print("4 - Удалить запись")
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

def Select_find():
    print("1 - Искать по фамилии")
    print("2 - Искать по имени")
    print("3 - Искать по отчеству")
    print("4 - Искать по дате рождения")
    print("5 - Искать по номеру телефона")
    act = input("Выберите действие --> ")
    temp = False

    while temp == False:
        if act == '1' or act == '2' or act == '3' or act == '4' or act == '5':
            temp = True
        else:
            act = input("Не верный выбор, введите цифру от 1 до 5 --> ")

    value = input("Введите фамилию ").split()
    value.append(act)

    return value

def Del_rec():
    print("Нужно вывести все записи что бы Вы могли выбрать номер удаляемой записи?")
    print("или у Вас есть номер нужной записи? если нужно вывести всю книжку нажмите 0")
    yes = input("или введите номер записи которую нужно удалить ")
    return yes