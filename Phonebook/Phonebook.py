print('''\t1. Открыть файл
\t2. Сохранить файл
\t3. Показать все контакты
\t4. Создать контакт
\t5. Изменить контакт
\t6. Найти контакт
\t7. Удалить контакт
\t8. Выход''')

phone_book = []
path = 'Python_homework\Phonebook\seminar8.txt'


def open_file():
    if phone_book:
        print("Файл уже загружен!")
    else:
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                cont = []
                for field in contact.split(';'):
                    cont.append(field.strip())
                phone_book.append(cont)
        print('Файл успешно загружен')


def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        for contact in phone_book:
            contact = ";".join(contact)
            file.write(f'{contact}\n')
    print("Файл сохранен!")


def show_contacts():
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')


def add_contact():
    print("Создание контакта:")
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))
    print(phone_book)


def modify_contact():
    number_contact = []
    modify_contact_list = []
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')
        number_contact.append(i)
    modify_number = int(input("Введите номер контакта для изменения:"))
    while modify_number not in number_contact:
        modify_number = int(input("Введите правильно номер контакта для изменения:"))
    modify_contact_list = phone_book[modify_number-1]
    print(modify_contact_list)
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.pop(modify_number-1)
    phone_book.insert(modify_number-1, list([name, phone, comment]))
    print(phone_book)



def search_contact():
    search = input('Введите ключевой элемент : ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)
            else:
                print("Контакт не найден!")


def delete_contact():
    number_contact = []
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')
        number_contact.append(i)
    del_number = int(input("Введите номер контакта для удаления:"))
    while del_number not in number_contact:
        del_number = int(input("Введите правильно номер контакта для удаления:"))
    phone_book.pop(del_number-1)
    print("Контакт удалён! Сохраните изменения!")


number = int(input('Введите пункт меню: '))
while number != 8 and number != 1:
    number = int(input('Сначала откройте файл или выйдите: '))
if number == 1:
    open_file()
else:
    print("Выход!")
    exit()

while True:
    number = int(input('Введите пункт меню: '))
    match number:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts()
        case 4:
            add_contact()
        case 5:
            modify_contact()
        case 6:
            search_contact()
        case 7:
            delete_contact()
        case 8:
            print("Выход!")
            break
        case _:
            print("Введите правильный пункт меню:")

