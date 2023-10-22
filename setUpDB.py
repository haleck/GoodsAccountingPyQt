from utils import *


def setUpTestUser():
    print("Создан тестовый пользователь: ", Users.create(
        name='test',
        surname='test',
        nickname='test',
        password='test',
        role=1
    ))


def setUpUnits():
    print('Создан товар: ', Units.create(name='Шт'))
    print('Создан товар: ', Units.create(name='Кг'))
    print('Создан товар: ', Units.create(name='Мл'))
    print('Создан товар: ', Units.create(name='Л'))
    print('Создан товар: ', Units.create(name='Грамм'))


def setUpManufacturers():
    print('Создан производитель: ', Manufacturers.create(name='Adidas'))
    print('Создан производитель: ', Manufacturers.create(name='Puma'))
    print('Создан производитель: ', Manufacturers.create(name='Obey'))
    print('Создан производитель: ', Manufacturers.create(name='H&M'))
    print('Создан производитель: ', Manufacturers.create(name='Hugo Boss'))
    print('Создан производитель: ', Manufacturers.create(name='Не выбран'))


def setUpCategories():
    print('Создана категория: ', Categories.create(name='Обувь'))
    print('Создана категория: ', Categories.create(name='Аксессуары'))
    print('Создана категория: ', Categories.create(name='Футболки'))
    print('Создана категория: ', Categories.create(name='Кофты'))
    print('Создана категория: ', Categories.create(name='Шапки'))
    print('Создана категория: ', Categories.create(name='Верхняя одежда'))
    print('Создана категория: ', Categories.create(name='Другое'))
    print('Создана категория: ', Categories.create(name='Не выбрана'))


def setUpRoles():
    print('Создана роль: ', Roles.create(name='Администратор'))
    print('Создана роль: ', Roles.create(name='Сотрудник'))
    print('Создана роль: ', Roles.create(name='Директор'))


def setUpStatuses():
    print('Создан статус: ', Statuses.create(name='Создан'))
    print('Создан статус: ', Statuses.create(name='Принят'))
    print('Создан статус: ', Statuses.create(name='Собирается'))
    print('Создан статус: ', Statuses.create(name='Отправлен'))
    print('Создан статус: ', Statuses.create(name='Принят на складе'))
    print('Создан статус: ', Statuses.create(name='Передан курьеру'))
    print('Создан статус: ', Statuses.create(name='Завершен'))


def setUpCausesToReturn():
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Повреждена упаковка'))
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Неполный комплект'))
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Не тот товар'))
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Поврежден товар'))
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Бракованный товар'))
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Другое'))
    print('Создана причина для возврата: ', CausesToReturn.create(cause='Не выбрана'))


def setUpActions():
    print('Создано действие: ', ActionsTable.create(action='Создание товара'))
    print('Создано действие: ', ActionsTable.create(action='Редактирование товара'))
    print('Создано действие: ', ActionsTable.create(action='Удаление товара'))
    print('Создано действие: ', ActionsTable.create(action='Проведение инвентаризации'))
    print('Создано действие: ', ActionsTable.create(action='Создание заказа'))
    print('Создано действие: ', ActionsTable.create(action='Редактирование заказа'))
    print('Создано действие: ', ActionsTable.create(action='Удаление заказа'))
    print('Создано действие: ', ActionsTable.create(action='Создание возврата'))
    print('Создано действие: ', ActionsTable.create(action='Редактирование возврата'))
    print('Создано действие: ', ActionsTable.create(action='Удаление возврата'))
    print('Создано действие: ', ActionsTable.create(action='Создание оприходования'))
    print('Создано действие: ', ActionsTable.create(action='Редактирование оприходования'))
    print('Создано действие: ', ActionsTable.create(action='Удаление оприходования'))
    print('Создано действие: ', ActionsTable.create(action='Создание списания'))
    print('Создано действие: ', ActionsTable.create(action='Редактирование списания'))
    print('Создано действие: ', ActionsTable.create(action='Удаление списания'))
    print('Создано действие: ', ActionsTable.create(action='Добавление сотрудника'))
    print('Создано действие: ', ActionsTable.create(action='Редактирование сотрудника'))
    print('Создано действие: ', ActionsTable.create(action='Удаление сотрудника'))


def setUpCausesToWriteOff():
    print("Создана причина для списания: ", CausesToWriteOff.create(cause='Истек срок годности'))
    print("Создана причина для списания: ", CausesToWriteOff.create(cause='Нарушены условия хранения'))
    print("Создана причина для списания: ", CausesToWriteOff.create(cause='Другое'))
    print("Создана причина для списания: ", CausesToWriteOff.create(cause='Не выбрана'))


