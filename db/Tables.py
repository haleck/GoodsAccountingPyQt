from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Statuses(Base):
    __tablename__ = 'Statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    orders = relationship('Orders', back_populates='status')


class Orders(Base):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    dateAndTime = Column(String)
    status = relationship('Statuses', back_populates='id')

    returns = relationship('Returns', back_populates='order')
    itemsInOrders = relationship('ItemsInOrders', back_populates='order_id')


class Returns(Base):
    __tablename__ = 'Returns'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)
    order = relationship('Orders', back_populates='id')

    ItemsInReturns = relationship('ItemsInReturns', back_populates='return_id')


class ItemsInOrders(Base):
    __tablename__ = 'ItemsInOrders'

    item_id = Column(Integer, ForeignKey('Items.id'))
    order_id = Column(Integer, ForeignKey('Orders.id'))
    __table_args__ = (
        UniqueConstraint('item_id', 'order_id', name='id'),
    )
    amount = Column(Integer)


class Items(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    category = relationship('Categories', back_populates='id')
    unit = relationship('Units', back_populates='id')
    price = Column(Integer)
    description = Column(String)
    manufacturer = relationship('Manufacturers', back_populates='id')
    amount = Column(Integer)

    itemsInOrders = relationship('ItemsInOrders', back_populates='item_id')
    itemsInReturns = relationship('ItemsInReturns', back_populates='item_id')
    itemsInInventory = relationship('ItemsInInventory', back_populates='item_id')
    writeOff = relationship('WriteOffs', back_populates='item')
    itemsInGetStocks = relationship('ItemsInGetStocks', back_populates='item_id')


class Categories(Base):
    __tablename__ = 'Categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    items = relationship('Items', back_populates='category')


class Units(Base):
    __tablename__ = 'Units'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    items = relationship('Items', back_populates='unit')


class Manufacturers(Base):
    __tablename__ = 'Manufacturers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    address = Column(String)
    phoneNumber = Column(String)

    items = relationship('Items', back_populates='manufacturer')


class ItemsInReturns(Base):
    __tablename__ = 'ItemsInReturns'

    item_id = Column(Integer, ForeignKey('Items.id'))
    return_id = Column(Integer, ForeignKey('Returns.id'))
    __table_args__ = (
        UniqueConstraint('item_id', 'return_id', name='id'),
    )
    cause = relationship('CausesToReturn', back_populates='id')


class CausesToReturn(Base):
    __tablename__ = 'CausesToReturn'

    id = Column(Integer, primary_key=True)
    cause = Column(String, unique=True)

    ItemsInReturns = relationship('ItemsInReturns', back_populates='cause')


class ItemsInInventory(Base):
    __tablename__ = 'InventoryItems'

    item_id = Column(Integer, ForeignKey('Items.id'))
    inventory_id = Column(Integer, ForeignKey('Inventory.id'))
    __table_args__ = (
        UniqueConstraint('item_id', 'inventory_id', name='id'),
    )
    currentAmount = Column(Integer)
    factAmount = Column(Integer)
    writeOffAmount = Column(Integer)


class Inventory(Base):
    __tablename__ = 'Inventory'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)

    ItemsInInventory = relationship('ItemsInInventory', back_populates='inventory_id')


class writeOffs(Base):
    __tablename__ = 'WriteOffs'

    id = Column(Integer, primary_key=True)
    item = relationship('Items', back_populates='id')
    cause = relationship('CausesToWriteOff', back_populates='id')
    dateAndTime = Column(String)


class CausesToWriteOff(Base):
    __tablename__ = 'CausesToWriteOff'

    id = Column(Integer, primary_key=True)
    cause = Column(String)

    writeOff = relationship('WriteOffs', back_populates='cause')


class ItemsInGetStocks(Base):
    __tablename__ = 'ItemsInGetstocks'

    item_id = Column(Integer, ForeignKey('Items.id'))
    getStocks_id = Column(Integer, ForeignKey('GetStocks.id'))
    __table_args__ = (
        UniqueConstraint('item_id', 'getStocks_id', name='id'),
    )
    amount = Column(Integer)
    goodQualityAmount = Column(Integer)


class GetStocks(Base):
    __tablename__ = 'GetStocks'

    id = Column(Integer, primary_key=True)
    dateAndTime = Column(String)

    itemsInGetStocks = relationship('ItemsInGetStocks', back_populates='getStocks_id')


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    nickname = Column(String)
    password = Column(String)
    phoneNumber = Column(String)
    role = relationship('Roles', back_populates='id')

    log = relationship('Log', back_populates='user')


class Roles(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    user = relationship('Users', back_populates='role')


class Log(Base):
    __tablename__ = 'Log'

    id = Column(Integer, primary_key=True)
    action = relationship('Actions', 'id')
    user = relationship('Users', back_populates='id')
    dateAndTime = Column(String)


class Actions(Base):
    __tablename__ = 'Actions'

    id = Column(Integer, primary_key=True)
    action = Column(String)

    log = relationship('Log', back_populates='action')