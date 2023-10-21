from peewee import Model, CharField, IntegerField, ForeignKeyField, PostgresqlDatabase, DeferredForeignKey

db = PostgresqlDatabase('dbb', user='zdiroog', password='password', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class Statuses(BaseModel):
    name = CharField(unique=True)


class Orders(BaseModel):
    address = CharField()
    dateAndTime = CharField()
    status = ForeignKeyField(Statuses, backref='order')


class Returns(BaseModel):
    dateAndTime = CharField()
    order = ForeignKeyField(Orders, backref='Return')


class ItemsInOrders(BaseModel):
    amount = IntegerField()
    item = DeferredForeignKey("Items", to_field='id', backref='itemInOrder')
    order = ForeignKeyField(Orders, to_field='id', backref='itemInOrder')


class Items(BaseModel):
    name = CharField(unique=True)
    price = IntegerField(null=True)
    description = CharField(null=True)
    amount = IntegerField(null=True)
    category = DeferredForeignKey("Categories", backref='item')
    unit = DeferredForeignKey("Units", backref='item')
    manufacturer = DeferredForeignKey("Manufacturers", backref='item')


class Categories(BaseModel):
    name = CharField(unique=True)


class Units(BaseModel):
    name = CharField(unique=True)


class Manufacturers(BaseModel):
    name = CharField(unique=True)
    address = CharField(null=True)
    phoneNumber = CharField(null=True)


class ItemsInReturns(BaseModel):
    amount = IntegerField()
    cause = DeferredForeignKey("CausesToReturn", backref='itemInReturn')
    item = ForeignKeyField(Items, to_field='id', backref='itemInReturn')
    return1 = ForeignKeyField(Returns, to_field='id', backref='itemInReturn')


class CausesToReturn(BaseModel):
    cause = CharField(unique=True)


class ItemsInInventory(BaseModel):
    currentAmount = IntegerField(null=True)
    factAmount = IntegerField()
    writeOffAmount = IntegerField(null=True)
    item = ForeignKeyField(Items, to_field='id', backref='itemInInventory')
    inventory = DeferredForeignKey("Inventory", to_field='id', backref='itemInInventory')


class Inventory(BaseModel):
    dateAndTime = CharField()


class WriteOffs(BaseModel):
    item = ForeignKeyField(Items, to_field='id', backref='writeOff')
    cause = DeferredForeignKey("CausesToWriteOff", backref='writeOff')
    amount = IntegerField()
    dateAndTime = CharField()


class CausesToWriteOff(BaseModel):
    cause = CharField(unique=True)


class ItemsInGetStocks(BaseModel):
    amount = IntegerField()
    goodQualityAmount = IntegerField(null=True)
    item = ForeignKeyField(Items, to_field='id', backref='itemInGetStock')
    getStock = DeferredForeignKey("GetStocks", to_field='id', backref='itemInGetStock')


class GetStocks(BaseModel):
    dateAndTime = CharField()


class Users(BaseModel):
    name = CharField()
    surname = CharField()
    patronymic = CharField(null=True)
    nickname = CharField(unique=True)
    password = CharField()
    phoneNumber = CharField(null=True)
    role = DeferredForeignKey("Roles", backref='user')


class Roles(BaseModel):
    name = CharField(unique=True)


class LogTable(BaseModel):
    action = DeferredForeignKey("ActionsTable", backref='log')
    user = ForeignKeyField(Users, backref='log')
    dateAndTime = CharField()


class ActionsTable(BaseModel):
    action = CharField(unique=True)
