from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, relationship

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
    itemInReturn = relationship('ItemsInReturns', back_populates='Return')


class ItemsInOrders(Base):
    __tablename__ = 'ItemsInOrders'

    item_id = Column(Integer, ForeignKey('Items.id'))
    order_id = Column(Integer, ForeignKey('Orders.id'))
    PrimaryKeyConstraint(item_id, order_id, name='id')
    amount = Column(Integer)

    order = relationship('Orders', back_populates='itemInOrder')
    item = relationship('Items', back_populates='itemInOrder')


class Items(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    description = Column(String)
    amount = Column(Integer)
    category_id = Column(Integer, ForeignKey('Categories.id'))
    unit_id = Column(Integer, ForeignKey('Units.id'))
    manufacturer_id = Column(Integer, ForeignKey('Manufacturers.id'))

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
    item_id = Column(Integer, ForeignKey('Items.id'))

    items = relationship('Items', back_populates='category')


class Units(Base):
    __tablename__ = 'Units'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    item_id = Column(Integer, ForeignKey('Item.id'))

    item = relationship('Items', back_populates='unit')


class Manufacturers(Base):
    __tablename__ = 'Manufacturers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    address = Column(String)
    phoneNumber = Column(String)

    item = relationship('Items', back_populates='manufacturer')


class ItemsInReturns(Base):
    __tablename__ = 'ItemsInReturns'

    item_id = Column(Integer, ForeignKey('Items.id'))
    return_id = Column(Integer, ForeignKey('Returns.id'))
    PrimaryKeyConstraint(item_id, return_id, name='id'),
    cause = relationship('CausesToReturn', back_populates='id')

    item = relationship('Items', back_populates='itemInReturn')
    Retrun = relationship('Returns', back_populates='itemInReturn')


class CausesToReturn(Base):
    __tablename__ = 'CausesToReturn'

    id = Column(Integer, primary_key=True)
    cause = Column(String, unique=True)

    itemsInReturn = relationship('ItemsInReturns', back_populates='cause')


class ItemsInInventory(Base):
    __tablename__ = 'InventoryItems'

    item_id = Column(Integer, ForeignKey('Items.id'))
    inventory_id = Column(Integer, ForeignKey('Inventory.id'))
    PrimaryKeyConstraint(item_id, inventory_id, name='id'),
    currentAmount = Column(Integer)
    factAmount = Column(Integer)
    writeOffAmount = Column(Integer)

    item = relationship('Items', back_populates='itemInInventory')
    inventory = relationship('Inventory', back_populates='itemInInventory')


class Inventory(Base):
    __tablename__ = 'Inventory'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)

    ItemsInInventory = relationship('ItemsInInventory', back_populates='inventory')


class writeOffs(Base):
    __tablename__ = 'WriteOffs'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('Items.id'))
    cause_id = Column(Integer, ForeignKey('Causes.id'))
    dateAndTime = Column(String)

    item = relationship('Items', back_populates='writeOff')
    cause = relationship('CausesToWriteOff', back_populates='writeOff')


class CausesToWriteOff(Base):
    __tablename__ = 'CausesToWriteOff'

    id = Column(Integer, primary_key=True)
    cause = Column(String)

    writeOff = relationship('WriteOffs', back_populates='cause')


class ItemsInGetStocks(Base):
    __tablename__ = 'ItemsInGetstocks'

    item_id = Column(Integer, ForeignKey('Items.id'))
    getStock_id = Column(Integer, ForeignKey('GetStocks.id'))
    PrimaryKeyConstraint(item_id, getStock_id, name='id'),
    amount = Column(Integer)
    goodQualityAmount = Column(Integer)

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
    patronymic = Column(String)
    nickname = Column(String)
    password = Column(String)
    phoneNumber = Column(String)
    role_id = Column(Integer, ForeignKey('Roles.id'))

    log = relationship('Log', back_populates='user')
    role = relationship('Roles', back_populates='user')


class Roles(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    user = relationship('Users', back_populates='role')


class Log(Base):
    __tablename__ = 'Log'

    id = Column(Integer, primary_key=True)
    action_id = Column(Integer, ForeignKey('Actons.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))
    dateAndTime = Column(String)

    action = relationship('Actions', 'log')
    user = relationship('Users', back_populates='log')


class Actions(Base):
    __tablename__ = 'Actions'

    id = Column(Integer, primary_key=True)
    action = Column(String)

    log = relationship('Log', back_populates='action')