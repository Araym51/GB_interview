from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Categories(Base):
    """
    Категории товаров
    Категории товаров. Написать запрос создания таблицы categories (с проверкой ее существования).
    Таблица должна содержать два поля: category_name (категория), category_description (описание).
    Все поля должны быть не пустыми. Поле category должно быть первичным ключом.
    """
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)
    category_description = Column(String(200), nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    def __repr__(self):
        return self.category_name


class Units(Base):
    """
    Единица измерения товаров
    Единицы измерения товаров. Написать запрос создания таблицы units с проверкой ее существования.
    Таблица должна содержать одно поле — unit (единица измерения).
    Оно должно быть не пустым и выступать первичным ключом.
    """
    __tablename__ = 'units of measure'
    unit_id = Column(Integer, primary_key=True)
    unit = Column(String(10), nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return self.unit


class Positions(Base):
    """
    Должности
    Должности. Написать запрос создания таблицы positions (с проверкой ее существования).
    Таблица должна содержать одно поле — position (должность).
    Оно должно быть не пустым и выступать первичным ключом.
    """
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position = Column(String(20), nullable=False)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return self.position


class Goods(Base):
    """
    Товары
    Написать запрос создания таблицы goods с проверкой ее существования.
    Таблица должна содержать четыре поля: good_id (номер товара — первичный ключ), good_name (название товара),
    good_unit (единица измерения товара — внешний ключ на таблицу units), good_cat
    (категория товара — внешний ключ на таблицу categories).
    """
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(50), nullable=False)
    good_unit = Column(Integer, ForeignKey('units.unit_id'))
    good_category = Column(Integer, ForeignKey('categories.category_id'))

    def __init__(self, good_name):
        self.good_name = good_name

    def __repr__(self):
        return self.good_name


class Employees(Base):
    """
    Сотрудники.
    Написать запрос создания таблицы employees с проверкой ее существования.
    Таблица должна содержать три поля: employee_id (номер сотрудника — первичный ключ),
    employee_fio (ФИО сотрудника), employee_position (должность сотрудника — внешний ключ на таблицу positions).
    """
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(50), nullable=False)
    employee_position = Column(Integer, ForeignKey('positions.position_id'))

    def __init__(self, employee_fio):
        self.employee_fio = employee_fio

    def __repr__(self):
        return self.employee_fio


class Vendors(Base):
    """
    Поставщики
    Написать запрос создания таблицы vendors с проверкой ее существования.
    Таблица должна содержать шесть полей: vendor_id (номер поставщика — первичный ключ),
    vendor_name (название поставщика), vendor_ownerchipform (форма собственности поставщика),
    vendor_address (адрес поставщика), vendor_phone (телефон поставщика), vendor_email (email поставщика).
    """
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(50), nullable=False)
    vendor_owner_chip_form = Column(String(50), nullable=False)
    vendor_address = Column(String(200), nullable=False)
    vendor_phone = Column(String(20), nullable=False)
    vendor_email = Column(String(20), nullable=False)

    def __init__(self, vendor_name, vendor_owner_chip_form,
                 vendor_address, vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_owner_chip_form = vendor_owner_chip_form
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return self.vendor_name