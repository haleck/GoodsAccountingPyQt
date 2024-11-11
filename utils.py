from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QCompleter

from Tables import *
from constants import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

db = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

db.connect()
db.create_tables([Statuses, Orders, Returns, ItemsInOrders, Items, Categories, Units,
                  Manufacturers, ItemsInReturns, CausesToReturn, ItemsInInventory, Inventory,
                  WriteOffs, CausesToWriteOff, ItemsInGetStocks, GetStocks, Users, Roles, LogTable, ActionsTable])


def fetchCategories():
    return [category.name for category in Categories.select()]


def findCategoryByName(name: str) -> int:
    return Categories.select().where(Categories.name == name)[0].id


def fetchManufacturers():
    return [manufacturer.name for manufacturer in Manufacturers.select()]


def findManufacturerByName(name: str) -> int:
    return Manufacturers.select().where(Manufacturers.name == name)[0].id


def fetchUnits():
    return [unit.name for unit in Units.select()]


def findUnitByName(name: str) -> int:
    return Units.select().where(Units.name == name)[0].id


def fetchRoles():
    return [role.name for role in Roles.select()]


def fetchStatuses():
    return [status.name for status in Statuses.select()]


def fetchCausesToReturn():
    return [cause.cause for cause in CausesToReturn.select()]


def fetchCausesToWriteOff():
    return [cause.cause for cause in CausesToWriteOff.select()]


def fetchInventActions():
    return ['Действия', 'Выделить все', 'Снять все', 'Показать выделенные', 'Показать все']


def fetchItems():
    items = []
    for item in Items.select():
        items.append(
            {
                'id': item.id,
                'name': item.name,
                "category": Categories.get(Categories.id == item.category).name,
                'unit': Units.get(Units.id == item.unit).name,
                'price': item.price,
                'description': item.description,
                'manufacturer': Manufacturers.get(Manufacturers.id == item.manufacturer).name,
                'amount': item.amount
            }
        )
    return items


def createItem(name='', price=0, description='', amount=0, category=None, unit=None, manufacturer=None):
    if name.isspace():
        raise Exception('Пустое название')
    if amount < 0:
        raise Exception('Значение количества ниже нуля')
    if int(price) < 0:
        raise Exception('Значение цены ниже нуля')
    return Items.create(
        name=name,
        price=price,
        description=description,
        amount=amount,
        category=category,
        unit=unit,
        manufacturer=manufacturer
    )


def updateItem(id, name=None, price=0, description='', amount=0, category=None, unit=None, manufacturer=None):
    if name.isspace():
        raise Exception('Пустое название')
    if amount < 0:
        raise Exception('Значение количества ниже нуля')
    if int(price) < 0:
        raise Exception('Значение цены ниже нуля')
    item = Items.get(Items.id == id)
    item.name = name
    item.price = price
    item.description = description
    item.amount = amount
    item.category = category
    item.unit = unit
    item.manufacturer = manufacturer
    return item.save()


def deleteItem(id):
    item = Items.get(Items.id == id)
    item.delete_instance()


def fetchActions():
    actions = []
    for action in LogTable.select():
        user = Users.get(Users.id == action.user)
        actions.append(
            {
                'id': action.id,
                'action': ActionsTable.get(ActionsTable.id == action.action).action,
                'employee': user.surname + " " + user.name + " " + user.patronymic if user.patronymic else user.surname + " " + user.name,
                'date': action.dateAndTime
            }
        )
    return actions


def findActionByDescription(description):
    return ActionsTable.select().where(ActionsTable.action == description)[0].id


def createNewLog(action=None, employee=None):
    if not action:
        raise Exception("Не указано действие для записи в журнал")
    action_id = findActionByDescription(action)
    return LogTable.create(
        action=action_id,
        user=employee,
        dateAndTime=datetime.now()
    )


def fetchEmployees():
    users = []
    for user in Users.select():
        users.append(
            {
                'id': user.id,
                "surname": user.surname,
                "name": user.name,
                "patronymic": user.patronymic,
                'role': user.role.name,
                'number': user.phoneNumber,
                'sex': 1,
                'username': user.nickname,
                "password": user.password
            }
        )
    return users


def createEmployee(surname=None, name=None, patronymic='', role='Сотрудник', number="", username=None, password=None):
    if surname.isspace():
        raise Exception('Поле фамилии не должно быть пустой строкой')
    if name.isspace():
        raise Exception('Поле имени не должно быть пустой строкой')
    if username.isspace():
        raise Exception('Поле username не должно быть пустой строкой')
    if password.isspace():
        raise Exception('Поле пароля не должно быть пустой строкой')
    return Users.create(
        name=name,
        surname=surname,
        patronymic=patronymic,
        nickname=username,
        password=password,
        phoneNumber=number,
        role=Roles.get(Roles.name == role)
    )


def updateEmployee(id, surname=None, name=None, patronymic='', role='Сотрудник', number="", username=None,
                   password=None):
    if surname.isspace():
        raise Exception('Поле фамилии не должно быть пустой строкой')
    if name.isspace():
        raise Exception('Поле имени не должно быть пустой строкой')
    if username.isspace():
        raise Exception('Поле username не должно быть пустой строкой')
    if password.isspace():
        raise Exception('Поле пароля не должно быть пустой строкой')
    role_id = Roles.get(Roles.name == role).id
    user = Users.get(Users.id == id)
    user.surname = surname
    user.name = name
    user.patronymic = patronymic
    user.role = role_id
    user.phoneNumber = number
    user.nickname = username
    user.password = password
    return user.save()


def deleteEmployee(id):
    return Users.delete_instance(Users.get(Users.id == id))


def fetchOrders():
    orders = []
    for order in Orders.select():
        orderItems = ItemsInOrders.select().where(ItemsInOrders.order == order.id)
        orders.append(
            {
                'id': order.id,
                'status': order.status.name,
                'address': order.address,
                'date': order.dateAndTime,
                'items': orderItems
            }
        )
    return orders


def fetchItemsInOrders(id):
    items = []
    for item in ItemsInOrders.select().where(ItemsInOrders.order == id):
        if item.item is None:
            items.append(
                {
                    'id': 0,
                    'name': "Удаленный товар",
                    "category": "",
                    'unit': "",
                    'price': "",
                    'description': "",
                    'manufacturer': "",
                    'amount': "?",
                    'amountToReturn': 0
                }
            )
        else:
            items.append(
                {
                    'id': item.item.id,
                    'name': item.item.name,
                    "category": Categories.get(Categories.id == item.item.category).name,
                    'unit': Units.get(Units.id == item.item.unit).name,
                    'price': item.item.price,
                    'description': item.item.description,
                    'manufacturer': Manufacturers.get(Manufacturers.id == item.item.manufacturer).name,
                    'amount': item.amount,
                    "amountToReturn": 0
                }
            )
    return items


def createOrder(address="", status="", items=[]):
    order = Orders.create(address=address, status=status, dateAndTime=datetime.now())
    for item in items:
        ItemsInOrders.create(
            item=item['id'],
            order=order.id,
            amount=item['amount'],
        )
        itemInDb = Items.get(Items.id == item['id'])
        itemInDb.amount = itemInDb.amount - item['amount']
        itemInDb.save()
    return 0


def fetchReturns():
    returns = []
    for Return in Returns.select():
        returns.append({
            'id': Return.id,
            "orderId": Return.order,
            "cause": Return.cause.cause,
            "date": Return.dateAndTime
        })
    return returns


def createReturn(order, cause, items):
    Return = Returns.create(
        dateAndTime=datetime.now(),
        cause=CausesToReturn.get(CausesToReturn.cause == cause),
        order=order,
    )
    for item in items:
        ItemsInReturns.create(
            item=item['id'],
            return1=Return,
            amount=item['amount']
        )
        itemInBD = Items.get(Items.id == item['id'])
        itemInBD.amount = itemInBD.amount + item['amount']
        itemInBD.save()
    return 0


# def getItemsByReturn(returnsData):
#     order_id = returnsData['orderId']
#     items = ItemsInOrders.select().where(ItemsInOrders.order == order_id)
#     itemsInOrders = []
#     for item in items:
#         itemsInOrders.append(
#             {
#                 "name": item.item.name,
#                 "manufacturer": item.item.manufacturer.name,
#                 "unit": item.item.unit.name,
#                 "amount": item.amount,
#                 "amountToReturn": 0
#             }
#         )
#     return itemsInOrders


def getItemsByReturn(returnsData):
    order_id = returnsData['orderId']
    items = ItemsInOrders.select().where(ItemsInOrders.order == order_id)
    itemsToReturn = ItemsInReturns.select().where(ItemsInReturns.return1 == returnsData['id'])
    itemsInOrders = []
    for item in items:
        amountToReturn = list(filter(lambda x: x.item == item.item, itemsToReturn))
        if len(amountToReturn) == 0:
            amountToReturn = 0
        else:
            amountToReturn = amountToReturn[0].amount
        itemsInOrders.append(
            {
                "name": item.item.name,
                "manufacturer": item.item.manufacturer.name,
                "unit": item.item.unit.name,
                "amount": item.amount,
                "amountToReturn": amountToReturn
            }
        )
    return itemsInOrders


def deleteOrder(id):
    order = Orders.get(Orders.id == id)
    items = ItemsInOrders.select().where(ItemsInOrders.order == id)
    for item in items:
        itemInBD = Items.get(Items.id == item.item)
        itemInBD.amount = itemInBD.amount + item.amount
        itemInBD.save()
    Orders.delete_instance(order)
    return 0


def updateOrder(id, address="", status="", items=[]):
    order = Orders.get(Orders.id == id)
    order.address = address
    order.status = status
    order.save()
    for item in items:
        itemInDB = Items.get(Items.id == item['id'])
        itemInDB.amount = item['amount']
        itemInDB.save(0)
    return 0


def fetchGetStocks():
    getStocks = []
    for getStock in GetStocks.select():
        [date, time] = getStock.dateAndTime.split(' ')
        getStocks.append(
            {
                'id': getStock.id,
                'date': date,
                'time': time,
                'items': [
                    {
                        'name': itemInGetStock.item.name,
                        'description': itemInGetStock.item.description,
                        'manufacturer': itemInGetStock.item.manufacturer.name,
                        'amount': itemInGetStock.amount,
                        'goodQuality': itemInGetStock.goodQualityAmount
                    } for itemInGetStock in ItemsInGetStocks.select().where(ItemsInGetStocks.getStock == getStock.id)
                ]
            }
        )
    return getStocks


def createGetStock(items):
    getStock = GetStocks.create(
        dateAndTime=datetime.now()
    )
    for item in items:
        itemInDB = Items.get(Items.name == item['name'])
        itemInDB.amount = itemInDB.amount + item['goodQuality']
        itemInDB.save()

        ItemsInGetStocks.create(
            amount=item['amount'],
            goodQualityAmount=item['goodQuality'],
            item=itemInDB,
            getStock=getStock
        )

    return 0


def fetchWriteOffs():
    writeOffs = []
    for writeOff in WriteOffs.select():
        writeOffs.append(
            {
                'id': writeOff.id,
                'date': writeOff.dateAndTime,
                'itemName': writeOff.item.name,
                'amount': str(writeOff.amount),
                'cause': writeOff.cause.cause,
                'manufacturer': writeOff.item.manufacturer.name
            }
        )
    return writeOffs


def createWriteOff(item='', cause='Не выбрана', amount=0):
    item = Items.get(Items.name == item)
    cause_id = CausesToWriteOff.get(CausesToWriteOff.cause == cause)
    if amount < 0:
        raise Exception("Значение количества ниже нуля")
    result = WriteOffs.create(
        item=item.id,
        cause=cause_id,
        amount=amount,
        dateAndTime=str(datetime.now())
    )
    item.amount = item.amount - amount
    item.save()
    return result


def updateWriteOff(id, item='', cause='Не выбрана', amount=0):
    item = Items.get(Items.name == item)
    cause_id = CausesToWriteOff.get(CausesToWriteOff.cause == cause)
    writeOff = WriteOffs.get(WriteOffs.id == id)
    if amount < 0:
        raise Exception("Значение количества ниже нуля")
    previous_amount = writeOff.amount
    writeOff.item = item.id
    writeOff.cause = cause_id
    writeOff.amount = amount
    item.amount = item.amount + (previous_amount - amount)
    item.save()
    return writeOff.save()


def deleteWriteOff(id):
    writeOff = WriteOffs.get(WriteOffs.id == id)
    writeOff.item.amount = writeOff.item.amount + writeOff.amount
    writeOff.item.save()
    return WriteOffs.delete_instance(writeOff)


def createInventory(items):
    inventory_id = Inventory.create(dateAndTime=datetime.now())
    for item in items:
        ItemsInInventory.create(
            currentAmount=item['currentAmount'],
            factAmount=item['factAmount'],
            writeOffAmount=item['writeOffAmount'],
            item=item['id'],
            inventory=inventory_id
        )
        item_ = Items.get(Items.id == item['id'])
        item_.amount = int(item['factAmount']) - int(item['writeOffAmount'])
        item_.save()
    return 0


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
