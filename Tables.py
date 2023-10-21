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