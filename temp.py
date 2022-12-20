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


print(value)
print(type(value))