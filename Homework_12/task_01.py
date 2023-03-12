import sqlite3


class PhoneBook:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.phone_number: str = phone_number


class Book:
    def __init__(self):
        self.bank_accounts: dict[str, PhoneBook] = {}

    def create_account(self, first_name, last_name, number):
        with sqlite3.connect('sqlite.db') as connection:
            connection.execute('''INSERT INTO user (first_name, last_name, number)
                                            VALUES 
                                            (?,?,?)''', (first_name, last_name, number))

    def show_accounts(self):
        with sqlite3.connect('sqlite.db') as connection:
            result = connection.execute('SELECT * FROM user  ORDER by last_name')
            for i in result.fetchall():
                print(i)

    def update_contacts(self, id, new_phone_number):
        with sqlite3.connect('sqlite.db') as connection:
            connection.execute('''UPDATE user
                                SET number = ?
                                WHERE id = ?;''', (new_phone_number, id))

class Controller:
    def __init__(self):
        self.book = Book()

    def run(self):
        while True:
            print('Выберите действие:')
            print('0. Выйти из программы')
            print('1. Добавить новый контакт')
            print('2. Вывести весь список контактов в алфавитном порядке')
            print('3. Обновить номер контакта')
            action = int(input('Выберите номер действия: '))
            if action == 0:
                print('До свидания!')
                break
            elif action == 1:
                first_name = input('Введите имя контакта: ')
                last_name = input('Введите фамилию контакта: ')
                phone_number = input('Введите номер телефона: ')
                self.book.create_account(first_name, last_name, phone_number)
                print(f'Контакт {first_name} {last_name} с номером телефона {phone_number} создан.')
            elif action == 2:
                self.book.show_accounts()

            elif action == 3:
                id = input('Введите номер контакта, который необходимо обновить: ')
                new_phone_number = input('Введите новый номер телефона: ')
                self.book.update_contacts(id, new_phone_number)
                print(f'Контакт №{id} обновлен. Новый номер:{new_phone_number}.')
            else:
                 print('Не поддерживаемая операция.')


if __name__ == '__main__':
    controller = Controller()
    controller.run()
