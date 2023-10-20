from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QCompleter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://zdiroog:password@localhost/db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()


def fetchCategories():
    return ["Не выбран", "Название категории 1", "Название категории 2", "Название категории 3"]


def fetchManufacturers():
    return ["Не выбран", "Производитель 1", "Производитель 2", "Производитель 3", "Производитель 4", "Производитель 5", ]


def fetchUnits():
    return ['Шт', 'Кг', 'Мл', 'Л', 'Грамм']


def fetchRoles():
    return ['Администратор', 'Сотрудник']


def fetchStatuses():
    return ['Создан', 'Принят', 'Собирается', 'Отправлен', 'Принят на складе', 'Передан курьеру', 'Завершен', ]

def fetchCauses():
    return ['Нарушена упаковка', "Неполный комплект", "Не тот товар", "Товар поврежден", "Бракованный товар", "Не выбрано"]

def fetchInventActions():
    return ['Действия', 'Выделить все', 'Снять все', 'Показать выделенные', 'Показать все']
def fetchItems():
    return [
        {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
        {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
        {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
        {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
        {'id': 5, 'name': 'Название товара 5', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 5', 'manufacturer': 'Производитель 2', 'amount': 1},
        {'id': 6, 'name': 'Название товара 6', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 6', 'manufacturer': 'Производитель 3', 'amount': 5},
        {'id': 7, 'name': 'Название товара 7', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 7', 'manufacturer': 'Производитель 3', 'amount': 1},
        {'id': 8, 'name': 'Название товара 8', 'category': 'Название категории 3', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 8', 'manufacturer': 'Производитель 4', 'amount': 10},
        {'id': 9, 'name': 'Название товара 9', 'category': 'Название категории 3', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 9', 'manufacturer': 'Производитель 5', 'amount': 8},
    ]


def fetchActions():
    return [
        {'id': 1, 'action': 'Создание товара', 'employee': 'Haleckiy Denis Aleksandrovich', 'date': '23.06.2023 16:30'},
        {'id': 2, 'action': 'Удаление товара', 'employee': 'Haleckiy Denis Aleksandrovich', 'date': '23.06.2023 18:40'},
        {'id': 3, 'action': 'Проведение инвентаризации', 'employee': 'Haleckiy Denis Aleksandrovich',
         'date': '23.06.2023 19:10'},
        {'id': 4, 'action': 'Создание товара', 'employee': 'Haleckiy Denis Aleksandrovich', 'date': '24.06.2023 10:00'},
        {'id': 5, 'action': 'Создание оприходования', 'employee': 'Haleckiy Denis Aleksandrovich',
         'date': '24.06.2023 12:12'},
        {'id': 6, 'action': 'Удаление товара', 'employee': 'Haleckiy Denis Aleksandrovich', 'date': '25.06.2023 09:30'},
        {'id': 7, 'action': 'Создание товара', 'employee': 'Haleckiy Denis Aleksandrovich', 'date': '25.06.2023 16:30'},
        {'id': 8, 'action': 'Редактирование товара', 'employee': 'Haleckiy Denis Aleksandrovich',
         'date': '25.06.2023 16:35'},
        {'id': 9, 'action': 'Создание товара', 'employee': 'Haleckiy Denis Aleksandrovich', 'date': '26.06.2023 19:00'},
    ]


def fetchEmployees():
    return [
        {'id': 1, 'surname': 'Haleckiy', 'name': 'Denis', 'patronymic': 'Aleksandrovich', 'role': 'Администратор',
         'number': '+79994006577', 'sex': 'male', 'username': 'Haleck991', 'password': 'SuperSecretPassword123'},
        {'id': 2, 'surname': 'Petronv', 'name': 'Anton', 'patronymic': 'Urievich', 'role': 'Сотрудник',
         'number': '+79294506577', 'sex': 'male', 'username': 'Petrov123', 'password': 'SecretPasswordPetrovv'},
        {'id': 3, 'surname': 'Ivanov', 'name': 'Semen', 'patronymic': 'Ivanovich', 'role': 'Сотрудник',
         'number': '+79794006554', 'sex': 'male', 'username': 'IvanovSemenIv', 'password': 'passIvanovSemen'},
        {'id': 4, 'surname': 'Sidorov', 'name': 'Vladislav', 'patronymic': 'Vladimirovich', 'role': 'Сотрудник',
         'number': '+79934006577', 'sex': 'male', 'username': 'SidorovVlad', 'password': 'vladPassSd'},
        {'id': 5, 'surname': 'Malcev', 'name': 'Roman', 'patronymic': 'Vladislavovich', 'role': 'Администратор',
         'number': '+79594916577', 'sex': 'male', 'username': 'Roman1222', 'password': 'RomanPass233'},
    ]


def fetchStock():
    return [
        {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1, 'reserved': 1},
        {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2, 'reserved': 1},
        {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1, 'reserved': 1},
        {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3, 'reserved': 2},
        {'id': 5, 'name': 'Название товара 5', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 5', 'manufacturer': 'Производитель 2', 'amount': 1, 'reserved': 1},
        {'id': 6, 'name': 'Название товара 6', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 6', 'manufacturer': 'Производитель 3', 'amount': 5, 'reserved': 3},
        {'id': 7, 'name': 'Название товара 7', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 7', 'manufacturer': 'Производитель 3', 'amount': 1, 'reserved': 1},
        {'id': 8, 'name': 'Название товара 8', 'category': 'Название категории 3', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 8', 'manufacturer': 'Производитель 4', 'amount': 10, 'reserved': 7},
        {'id': 9, 'name': 'Название товара 9', 'category': 'Название категории 3', 'unit': 'Шт.', 'price': 123,
         'description': 'Описание товара 9', 'manufacturer': 'Производитель 5', 'amount': 8, 'reserved': 2},
    ]


def fetchOrders():
    return [
        {'id': 1, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '24.09.2023',
         'items': [
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},{'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},{'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},{'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
         ]},
        {'id': 2, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '25.09.2023',
         'items': [
             {'id': 1, 'name': '1Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': '1Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': '1Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': '1Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': '1Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': '1Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': '1Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': '1Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': '1Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': '1Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': '1Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': '1Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': '1Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
             {'id': 2, 'name': '1Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': '1Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': '1Название товара 10', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
         ]},
        {'id': 3, 'status': 'Принят', 'address': 'a long long address line 4 ex. 12322', 'date': '24.11.2023',
         'items': []},
        {'id': 4, 'status': 'Собирается', 'address': 'a long long address line 4 ex. 12322', 'date': '25.11.2023',
         'items': []},
        {'id': 5, 'status': 'Завершен', 'address': 'a long long address line 4 ex. 12322', 'date': '26.11.2023',
         'items': []},
        {'id': 6, 'status': 'Передан курьеру', 'address': 'a long long address line 4 ex. 12322', 'date': '29.11.2023',
         'items': []},
        {'id': 7, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '24.09.2023',
         'items': [
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
         ]},
        {'id': 8, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '25.09.2023',
         'items': []},
        {'id': 9, 'status': 'Принят', 'address': 'a long long address line 4 ex. 12322', 'date': '24.11.2023',
         'items': []},
        {'id': 10, 'status': 'Собирается', 'address': 'a long long address line 4 ex. 12322', 'date': '25.11.2023',
         'items': []},
        {'id': 11, 'status': 'Завершен', 'address': 'a long long address line 4 ex. 12322', 'date': '26.11.2023',
         'items': []},
        {'id': 12, 'status': 'Передан курьеру', 'address': 'a long long address line 4 ex. 12322', 'date': '29.11.2023',
         'items': []},
        {'id': 13, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '24.09.2023',
         'items': [
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
         ]},
        {'id': 14, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '25.09.2023',
         'items': []},
        {'id': 15, 'status': 'Принят', 'address': 'a long long address line 4 ex. 12322', 'date': '24.11.2023',
         'items': []},
        {'id': 16, 'status': 'Собирается', 'address': 'a long long address line 4 ex. 12322', 'date': '25.11.2023',
         'items': []},
        {'id': 17, 'status': 'Завершен', 'address': 'a long long address line 4 ex. 12322', 'date': '26.11.2023',
         'items': []},
        {'id': 18, 'status': 'Передан курьеру', 'address': 'a long long address line 4 ex. 12322', 'date': '29.11.2023',
         'items': []},
        {'id': 19, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '24.09.2023',
         'items': [
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
         ]},
        {'id': 20, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '25.09.2023',
         'items': []},
        {'id': 21, 'status': 'Принят', 'address': 'a long long address line 4 ex. 12322', 'date': '24.11.2023',
         'items': []},
        {'id': 22, 'status': 'Собирается', 'address': 'a long long address line 4 ex. 12322', 'date': '25.11.2023',
         'items': []},
        {'id': 23, 'status': 'Завершен', 'address': 'a long long address line 4 ex. 12322', 'date': '26.11.2023',
         'items': []},
        {'id': 24, 'status': 'Передан курьеру', 'address': 'a long long address line 4 ex. 12322', 'date': '29.11.2023',
         'items': []},
        {'id': 25, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '24.09.2023',
         'items': [
             {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
             {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
             {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
             {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
              'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
         ]},
        {'id': 26, 'status': 'Создан', 'address': 'a long long address line 4 ex. 12322', 'date': '25.09.2023',
         'items': []},
        {'id': 27, 'status': 'Принят', 'address': 'a long long address line 4 ex. 12322', 'date': '24.11.2023',
         'items': []},
        {'id': 28, 'status': 'Собирается', 'address': 'a long long address line 4 ex. 12322', 'date': '25.11.2023',
         'items': []},
        {'id': 29, 'status': 'Завершен', 'address': 'a long long address line 4 ex. 12322', 'date': '26.11.2023',
         'items': []},
        {'id': 30, 'status': 'Передан курьеру', 'address': 'a long long address line 4 ex. 12322', 'date': '29.11.2023',
         'items': []},
    ]

def fetchReturns():
    return [
        {'id': 1, 'orderId': 1, 'cause': 'Нарушена упаковка', 'date': '12.04.2023'},
        {'id': 2, 'orderId': 2, 'cause': 'Бракованный товар', 'date': '15.04.2023'},
        {'id': 3, 'orderId': 3, 'cause': 'Не полный комплект', 'date': '22.04.2023'},
        {'id': 4, 'orderId': 4, 'cause': 'Нарушена упаковка', 'date': '27.04.2023'},
        {'id': 5, 'orderId': 5, 'cause': 'Не полный комплект', 'date': '02.05.2023'},
    ]

def getItemsByOrderId(id: str):
    order = filter(lambda x: x['id'] == id, fetchOrders())
    order = list(order)[0]
    return order['items']

def fetchGetStocks():
    return [
        {'id': 1, 'date': '23.06.2023', 'time': '20:10', 'items': [
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
            {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
            {'id': 2, 'name': 'Название товара 2', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 2', 'manufacturer': 'Производитель 1', 'amount': 2},
            {'id': 3, 'name': 'Название товара 3', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 3', 'manufacturer': 'Производитель 2', 'amount': 1},
            {'id': 4, 'name': 'Название товара 4', 'category': 'Название категории 2', 'unit': 'Шт.', 'price': 123,
             'description': 'Описание товара 4', 'manufacturer': 'Производитель 2', 'amount': 3},
        ]},
        {'id': 2, 'date': '23.06.2023', 'time': '20:15', 'items': []},
        {'id': 3, 'date': '24.06.2023', 'time': '15:40', 'items': []},
        {'id': 4, 'date': '24.06.2023', 'time': '16:30', 'items': []},
        {'id': 5, 'date': '24.06.2023', 'time': '16:40', 'items': []},
    ]

def fetchWriteOffs():
    return [
        {'id': 1, 'date': '23.06.2023', 'itemName': 'Молоко', 'amount': 2, 'cause': 'Нарушена упаковки', 'manufacturer': 'Производитель товара 1'},
        {'id': 2, 'date': '23.06.2023', 'itemName': 'Кефир', 'amount': 2, 'cause': 'Срок годности', 'manufacturer': 'Производитель товара 2'},
        {'id': 3, 'date': '24.06.2023', 'itemName': 'Сгущенка', 'amount': 2, 'cause': 'Срок годности', 'manufacturer': 'Производитель товара 3'},
        {'id': 4, 'date': '25.06.2023', 'itemName': 'Сыр', 'amount': 2, 'cause': 'Нарушена упаковки', 'manufacturer': 'Производитель товара 4'},
        {'id': 5, 'date': '25.06.2023', 'itemName': 'Торт', 'amount': 1, 'cause': 'Срок годности', 'manufacturer': 'Производитель товара 5'},
    ]


def perform_search(search_query ,table):
    for row in range(table.rowCount()):
        text_in_row = ""
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item:
                text_in_row += item.text()

        if search_query.lower() in text_in_row.lower():
            table.setRowHidden(row, False)
        else:
            table.setRowHidden(row, True)


def addItemCompleters(lineEdit):
    completer = QCompleter()
    word_list = fetchItems()
    completer_model = QStandardItemModel()
    completer.setModel(completer_model)
    for item in word_list:
        list_item = QStandardItem(item['name'])
        completer_model.appendRow(list_item)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    completer.popup().setStyleSheet(
        "background-color: rgb(91, 91, 91); color: rgb(217, 217, 217); border: 1px solid rgb(66, 66, 66);")
    lineEdit.setCompleter(completer)
