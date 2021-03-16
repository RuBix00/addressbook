# Работает из cmd. Можно добавлять, изменять, удалять и искать контакты. Контакты должны сохраняться на диске
# Для копирования файлов, при помощи метода copyfile
import shutil
import time
from colorama import init, Style

init()

class Addressbook():
    # Работает
    def __init__(self, name, number):
        """Initialtion

        Create new contact with name and number and add it to addressbook"""
        self.name = name
        self.number = number
        print('Добавлен новый контакт. Имя - {0}, номер телефона - {1}\n'.format(self.name, self.number))
        file = open('Addressbook.txt', 'a')
        file1 = open('clipboard.txt', 'a')
        file.write('Номер телефона - {0}, имя - {1}\n'.format(self.number, self.name))
        file1.write('Номер телефона - {0}, имя - {1}\n'.format(self.number, self.name))
        file.close()
        file1.close()

    # Работает
    @staticmethod
    def change(name, number, name1, number1):
        """Change contact, staticmethod

        You change name and number of the contact. Using shutil.copyfile"""
        file = open('Addressbook.txt', 'r+')
        file1 = open('clipboard.txt', 'r+')
        for lines in file1.readlines():
            if lines != 'Номер телефона - {0}, имя - {1}\n'.format(number, name):
                file.write(lines)
            elif lines == 'Номер телефона - {0}, имя - {1}\n'.format(number, name):
                file.write('Номер телефона - {0}, имя - {1}\n'.format(number1, name1))
        file.close()
        file1.close()
        shutil.copyfile('Addressbook.txt', 'clipboard.txt')
        print('Аккаунт {0}, с номером {1}, изменён на {2}, с номером {3}\n'.format(name, number, name1, number1))

    # Работает
    @staticmethod
    def delete(name, number):
        """Delete contact, staticmethod

        You delete the contact, finding by name and number"""
        file = open('Addressbook.txt', 'w')
        file1 = open('clipboard.txt', 'r+')
        for lines in file1.readlines():
            if lines != 'Номер телефона - {0}, имя - {1}\n'.format(number, name):
                file.write(lines)
            elif lines == 'Номер телефона - {0}, имя - {1}\n'.format(number, name):
                file.write(lines.replace('Номер телефона - {0}, имя - {1}\n'.format(number, name), ''))
        file.close()
        file1.close()
        shutil.copyfile('Addressbook.txt', 'clipboard.txt')
        print('Аккаунт {0}, с номром {1} был успешно удалён\n'.format(name, number))

    # Работает
    @staticmethod
    def find(name):
        file = open('Addressbook.txt', 'r+')
        file1 = open('clipboard.txt', 'r+')
        for lines in file1.readlines():
            if name in lines:
                print(lines + '\n')
        file.close()
        file1.close()


while True:
    print(Style.DIM + '''Выберните действие:
    1. Добавить
    2. Изменить
    3. Удалить
    4. Найти
    0. Выйти\n''')
    action = input('Введите действие:')
    if action == '1' or action == 'Добавить':
        name = input('Введите имя: ')
        number = input('Введите номер: ')
        pers1 = Addressbook(name, number)
    elif action == '2' or action == 'Изменить':
        name = input('Введите имя контакта, которое хотите изменить: ')
        number = input('Введите номер контакта, который хотите изменить: ')
        name1 = input('Введите новое имя контакта: ')
        number1 = input('Введите новое имя контакта: ')
        Addressbook.change(name, number, name1, number1)
    elif action == '3' or action == 'Удалить':
        name = input('Введите имя контакта, который хотите удалить: ')
        number = input('Введите номер контакта, который хотите удалить: ')
        Addressbook.delete(name, number)
    elif action == '4' or action == 'Найти':
        name = input('Введите имя контакта, который хотите найти\n')
    elif action == '0' or action == 'Выйти':
        print('Завершение работы')
        time.sleep(3)
        break
    else:
        print('Возможно вы ввели что-то некоректно, попытайтесь заново\n')