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
    status = ForeignKeyField(Statuses, backref='order', on_delete="SET NULL", null=True)


class CausesToReturn(BaseModel):
    cause = CharField(unique=True)


class Returns(BaseModel):
    dateAndTime = CharField()
    cause = ForeignKeyField(CausesToReturn, backref='itemInReturn', on_delete="SET NULL", null=True)
    order = ForeignKeyField(Orders, backref='Return', on_delete="CASCADE")


class Categories(BaseModel):
    name = CharField(unique=True)


class Units(BaseModel):
    name = CharField(unique=True)


class Manufacturers(BaseModel):
    name = CharField(unique=True)
    address = CharField(null=True)
    phoneNumber = CharField(null=True)


class Items(BaseModel):
    name = CharField(unique=True)
    price = IntegerField(null=True)
    description = CharField(null=True)
    amount = IntegerField(null=True)
    category = ForeignKeyField(Categories, backref='item', on_delete="SET NULL", null=True)
    unit = ForeignKeyField(Units, backref='item', on_delete="SET NULL", null=True)
    manufacturer = ForeignKeyField(Manufacturers, backref='item', on_delete="SET NULL", null=True)


class ItemsInOrders(BaseModel):
    amount = IntegerField()
    item = ForeignKeyField(Items, to_field='id', backref='itemInOrder', on_delete="SET NULL", null=True)
    order = ForeignKeyField(Orders, to_field='id', backref='itemInOrder', on_delete="CASCADE")


class ItemsInReturns(BaseModel):
    amount = IntegerField()
    item = ForeignKeyField(Items, to_field='id', backref='itemInReturn', on_delete="SET NULL", null=True)
    return1 = ForeignKeyField(Returns, to_field='id', backref='itemInReturn', on_delete="CASCADE")


class Inventory(BaseModel):
    dateAndTime = CharField()


class ItemsInInventory(BaseModel):
    currentAmount = IntegerField(null=True)
    factAmount = IntegerField()
    writeOffAmount = IntegerField(null=True)
    item = ForeignKeyField(Items, to_field='id', backref='itemInInventory', on_delete="SET NULL", null=True)
    inventory = ForeignKeyField(Inventory, to_field='id', backref='itemInInventory', on_delete="CASCADE")


class CausesToWriteOff(BaseModel):
    cause = CharField(unique=True)


class WriteOffs(BaseModel):
    item = ForeignKeyField(Items, to_field='id', backref='writeOff', on_delete="CASCADE")
    cause = ForeignKeyField(CausesToWriteOff, backref='writeOff', on_delete="SET NULL", null=True)
    amount = IntegerField()
    dateAndTime = CharField()


class GetStocks(BaseModel):
    dateAndTime = CharField()


class ItemsInGetStocks(BaseModel):
    amount = IntegerField()
    goodQualityAmount = IntegerField(null=True)
    item = ForeignKeyField(Items, to_field='id', backref='itemInGetStock', on_delete="SET NULL", null=True)
    getStock = ForeignKeyField(GetStocks, to_field='id', backref='itemInGetStock', on_delete="CASCADE")


class Roles(BaseModel):
    name = CharField(unique=True)


class Users(BaseModel):
    name = CharField()
    surname = CharField()
    patronymic = CharField(null=True)
    nickname = CharField(unique=True)
    password = CharField()
    phoneNumber = CharField(null=True)
    role = ForeignKeyField(Roles, backref='user', on_delete="RESTRICT")


class ActionsTable(BaseModel):
    action = CharField(unique=True)


class LogTable(BaseModel):
    action = ForeignKeyField(ActionsTable, backref='log', on_delete="SET NULL", null=True)
    user = ForeignKeyField(Users, backref='log', on_delete="SET NULL", null=True)
    dateAndTime = CharField()
