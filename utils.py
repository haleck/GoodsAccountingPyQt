from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QCompleter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Statuses(Base):
    __tablename__ = 'Statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    order = relationship('Orders', back_populates='status')


class Orders(Base):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    dateAndTime = Column(String)
    status_id = Column(Integer, ForeignKey('Statuses.id'))

    status = relationship('Statuses', back_populates='order')
    Return = relationship('Returns', back_populates='order')
    itemInOrder = relationship('ItemsInOrders', back_populates='order')


class Returns(Base):
    __tablename__ = 'Returns'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)
    order_id = Column(Integer, ForeignKey('Orders.id'))

    order = relationship('Orders', back_populates='Return')
    itemInReturn = relationship('ItemsInReturns', back_populates='return1')


class ItemsInOrders(Base):
    __tablename__ = 'ItemsInOrders'

    item_id = Column(Integer, ForeignKey('Items.id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('Orders.id'), primary_key=True)
    amount = Column(Integer)

    order = relationship('Orders', back_populates='itemInOrder')
    item = relationship('Items', back_populates='itemInOrder')


class Items(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    amount = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey('Categories.id'), nullable=True)
    unit_id = Column(Integer, ForeignKey('Units.id'), nullable=True)
    manufacturer_id = Column(Integer, ForeignKey('Manufacturers.id'), nullable=True)

    category = relationship('Categories', back_populates='item')
    unit = relationship('Units', back_populates='item')
    manufacturer = relationship('Manufacturers', back_populates='item')
    itemInOrder = relationship('ItemsInOrders', back_populates='item')
    itemInReturn = relationship('ItemsInReturns', back_populates='item')
    itemInInventory = relationship('ItemsInInventory', back_populates='item')
    writeOff = relationship('WriteOffs', back_populates='item')
    itemInGetStock = relationship('ItemsInGetStocks', back_populates='item')


class Categories(Base):
    __tablename__ = 'Categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    item = relationship('Items', back_populates='category')


class Units(Base):
    __tablename__ = 'Units'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    item = relationship('Items', back_populates='unit')


class Manufacturers(Base):
    __tablename__ = 'Manufacturers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    address = Column(String, nullable=True)
    phoneNumber = Column(String, nullable=True)

    item = relationship('Items', back_populates='manufacturer')


class ItemsInReturns(Base):
    __tablename__ = 'ItemsInReturns'

    item_id = Column(Integer, ForeignKey('Items.id'), primary_key=True)
    return_id = Column(Integer, ForeignKey('Returns.id'), primary_key=True)
    amount = Column(String)
    cause_id = Column(Integer, ForeignKey('CausesToReturn.id'))

    cause = relationship('CausesToReturn', back_populates='itemInReturn')
    item = relationship('Items', back_populates='itemInReturn')
    return1 = relationship('Returns', back_populates='itemInReturn')


class CausesToReturn(Base):
    __tablename__ = 'CausesToReturn'

    id = Column(Integer, primary_key=True)
    cause = Column(String, unique=True)

    itemInReturn = relationship('ItemsInReturns', back_populates='cause')


class ItemsInInventory(Base):
    __tablename__ = 'ItemsInInventory'

    item_id = Column(Integer, ForeignKey('Items.id'), primary_key=True)
    inventory_id = Column(Integer, ForeignKey('Inventory.id'), primary_key=True)
    currentAmount = Column(Integer, nullable=True)
    factAmount = Column(Integer)
    writeOffAmount = Column(Integer, nullable=True)

    item = relationship('Items', back_populates='itemInInventory')
    inventory = relationship('Inventory', back_populates='itemInInventory')


class Inventory(Base):
    __tablename__ = 'Inventory'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)

    itemInInventory = relationship('ItemsInInventory', back_populates='inventory')


class WriteOffs(Base):
    __tablename__ = 'WriteOffs'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('Items.id'))
    cause_id = Column(Integer, ForeignKey('CausesToWriteOff.id'))
    amount = Column(Integer)
    dateAndTime = Column(String)

    item = relationship('Items', back_populates='writeOff')
    cause = relationship('CausesToWriteOff', back_populates='writeOff')


class CausesToWriteOff(Base):
    __tablename__ = 'CausesToWriteOff'

    id = Column(Integer, primary_key=True)
    cause = Column(String, unique=True)

    writeOff = relationship('WriteOffs', back_populates='cause')


class ItemsInGetStocks(Base):
    __tablename__ = 'ItemsInGetstocks'

    item_id = Column(Integer, ForeignKey('Items.id'), primary_key=True)
    getStock_id = Column(Integer, ForeignKey('GetStocks.id'), primary_key=True)
    amount = Column(Integer)
    goodQualityAmount = Column(Integer, nullable=True)

    item = relationship('Items', back_populates='itemInGetStock')
    getStock = relationship('GetStocks', back_populates='itemInGetStock')


class GetStocks(Base):
    __tablename__ = 'GetStocks'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)

    itemInGetStock = relationship('ItemsInGetStocks', back_populates='getStock')


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String, nullable=True)
    nickname = Column(String, unique=True)
    password = Column(String)
    phoneNumber = Column(String, nullable=True)
    role_id = Column(Integer, ForeignKey('Roles.id'))

    log = relationship('LogTable', back_populates='user')
    role = relationship('Roles', back_populates='user')


class Roles(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    user = relationship('Users', back_populates='role')


class LogTable(Base):
    __tablename__ = 'LogTable'

    id = Column(Integer, primary_key=True)
    action_id = Column(Integer, ForeignKey('ActionsTable.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    dateAndTime = Column(String)

    action = relationship('ActionsTable', 'log')
    user = relationship('Users', back_populates='log')


class ActionsTable(Base):
    __tablename__ = 'ActionsTable'

    id = Column(Integer, primary_key=True)
    action = Column(String, unique=True)

    log = relationship('LogTable', back_populates='action')

db_url = "postgresql://zdiroog:password@localhost/db"
engine = create_engine(db_url)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(Statuses(name='Создан'))

itemsQuery = session.query(Statuses)
print(itemsQuery)


def fetchCategories():
    return ["Не выбран", "Название категории 1", "Название категории 2", "Название категории 3"]


def fetchManufacturers():
    return ["Не выбран", "Производитель 1", "Производитель 2", "Производитель 3", "Производитель 4",
            "Производитель 5", ]


def fetchUnits():
    return ['Шт', 'Кг', 'Мл', 'Л', 'Грамм']


def fetchRoles():
    return ['Администратор', 'Сотрудник']


def fetchStatuses():
    return ['Создан', 'Принят', 'Собирается', 'Отправлен', 'Принят на складе', 'Передан курьеру', 'Завершен', ]


def fetchCausesToReturn():
    return ['Нарушена упаковка', "Неполный комплект", "Не тот товар", "Товар поврежден", "Бракованный товар",
            "Не выбрано"]


def fetchCausesToWriteOff():
    return ["Не выбрано", "Другое", "Истек срок годности", "Нарушены условия хранения"]


def fetchInventActions():
    return ['Действия', 'Выделить все', 'Снять все', 'Показать выделенные', 'Показать все']


def fetchItems():
    # {'id': 1, 'name': 'Название товара 1', 'category': 'Название категории 1', 'unit': 'Шт.', 'price': 123,
    #          'description': 'Описание товара 1', 'manufacturer': 'Производитель 1', 'amount': 1},
    return itemsQuery


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
        {'id': 1, 'date': '23.06.2023', 'itemName': 'Молоко', 'amount': 2, 'cause': 'Нарушена упаковки',
         'manufacturer': 'Производитель товара 1'},
        {'id': 2, 'date': '23.06.2023', 'itemName': 'Кефир', 'amount': 2, 'cause': 'Срок годности',
         'manufacturer': 'Производитель товара 2'},
        {'id': 3, 'date': '24.06.2023', 'itemName': 'Сгущенка', 'amount': 2, 'cause': 'Срок годности',
         'manufacturer': 'Производитель товара 3'},
        {'id': 4, 'date': '25.06.2023', 'itemName': 'Сыр', 'amount': 2, 'cause': 'Нарушена упаковки',
         'manufacturer': 'Производитель товара 4'},
        {'id': 5, 'date': '25.06.2023', 'itemName': 'Торт', 'amount': 1, 'cause': 'Срок годности',
         'manufacturer': 'Производитель товара 5'},
    ]


def perform_search(search_query, table):
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
