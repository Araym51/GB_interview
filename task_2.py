"""
1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.product_name} costs {self.product_price} rub.')


item = ItemDiscountReport('Zotac rtx 3070', 43000)
item.get_parent_data()

"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.__product_name} costs {self.__product_price} rub.')


item = ItemDiscountReport('MSI rtx 3070', 53000)
# item.get_parent_data()

# Traceback (most recent call last):
#   File "C:\Users\Terra\PycharmProjects\GB_interview\task_2.py", line 39, in <module>
#     item.get_parent_data()
#   File "C:\Users\Terra\PycharmProjects\GB_interview\task_2.py", line 35, in get_parent_data
#     print(f'{self.__product_name} costs {self.__product_price} rub.')
# AttributeError: 'ItemDiscountReport' object has no attribute '_ItemDiscountReport__product_name'


"""
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. 
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    def get_parent_data(self):
        print(f'{self.__product_name} costs {self.__product_price} rub.')


item = ItemDiscountReport('MSI rtx 3070', 53000)
item.get_parent_data()

"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, 
и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий 
метод родительского класса и функцию дочернего (функция, отвечающая за отображение информации 
о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    def set_price(self, product_price):
        self.__product_price = product_price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    def get_parent_data(self):
        print(f'{self.__product_name} costs {self.__product_price} rub.')


item = ItemDiscountReport('Asus rtx 3070', 47000)
item.set_price(48000)
item.get_parent_data()

"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве 
аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса 
(метод init, в который должна передаваться переменная — скидка), и перегрузку метода str 
дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена 
товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и 
родительский классы (вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscountReport(ItemDiscount):
    def __init__(self, product_name, product_price, discount):
        self.__product_name = product_name
        self.__product_price = product_price
        self.discount = discount

    def get_parent_data(self):
        print(
            f'{self.__product_name} costs {self.__product_price - (self.__product_price * self.discount) / 100} rub. '
                                                                                                      f'with discount')


item = ItemDiscountReport('Asus rtx 3070', 47000, 50)
item.set_price(48000)
item.get_parent_data()

"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс 
ItemDiscountReport на два класса. Инициализировать классы необязательно. Внутри каждого 
поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара, 
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
"""

class ItemDiscount:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price


class ItemDiscountReportOne(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.product_name} costs {self.product_price} rub.')



class ItemDiscountReportTwo(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.product_name} costs {self.product_price} rub.')


first_item = ItemDiscountReportOne('Nvidia 4080', 100000)
first_item.get_parent_data()

second_item = ItemDiscountReportTwo('Nvidia 4090', 200000)
second_item.get_parent_data()

for method in (first_item, second_item):
    method.get_parent_data()


def method_handler(class_object):
    class_object.get_parent_data()


method_handler(first_item)
method_handler(second_item)
