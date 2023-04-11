import os
import pprint
import random

pp = pprint.PrettyPrinter()
"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""


def table(x, y):
    """
    :param x: количество элементов по оси х
    :param y: количество элементов по оси у
    :return: таблица умножения
    """
    for i in range(y + 1):
        row = []
        for j in range(x + 1):
            row.append(j) if i == 0 else (row.append(i) if j == 0 else row.append(i * j))
        print('\t'.join([str(_) for _ in row]))


# table(5, 10)


"""
2. Дополнить следующую функцию недостающим кодом:
"""
def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    def get_folders_and_files(sPath):
        items = []
        for files_and_folders in os.listdir(sPath):
            name = os.path.join(os.path.abspath(sPath), files_and_folders)
            items.append((os.path.abspath(sPath), files_and_folders)) if os.path.isfile(name) else items.extend(
                get_folders_and_files(name))
        return items
    return pp.pprint(get_folders_and_files(sPath))


# вместо ara подставьте свой username
# print_directory_contents('/home/ara/PycharmProjects/')


"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное 
число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. 
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. 
Вывести содержимое созданных списка и словаря.
"""
def gen(start, finish):
    if start == 0 or finish == 0:
        return 'Ноль в качестве аргумента запрещен'
    else:
        item_list = []
        item_dict = {}
        for _ in range(10):
            value = int((finish - start) * random.random() + start)
            item_list.append(value)
            item_dict.update({f'elem_{value}': value})
        return item_list, item_dict


# pp.pprint(gen(2, 100))


"""
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. 
Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка: 
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). 
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада. 
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). 
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока. 
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет 
по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
"""
def get_percent(deposit, months):
    if months not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= deposit < rate['end_sum']:
            return rate[months]

    return False


def deposit_sum(deposit, months):
    percent = get_percent(deposit, months)
    if not percent:
        return 'Введите данные согласно тарифной сетки'

    total_profit = deposit
    for i in range(months):
        profit = total_profit * percent / 100 / 12
        total_profit += profit

    return round(total_profit, 2)

print(deposit_sum(1000, 11,))
print(deposit_sum(10, 12,))
print(deposit_sum(10000, 12,))


"""
5. Усовершенствовать программу «Банковский депозит». 
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. 
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы. 
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. 
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. 
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), 
а главная функция — общую сумму по вкладу на конец периода.
"""
def chargable_deposit(deposit, months, charge=0):
    percent = get_percent(deposit, months)
    if not percent:
        return 'Введите данные согласно тарифной сетки'

    total_profit = deposit
    for i in range(months):
        profit = total_profit * percent / 100 / 12
        total_profit += profit
        if i != 0 and i != months - 1:
            total_profit += charge + charge * percent / 100 / 12

    return round(total_profit, 2)


print(chargable_deposit(1000, 12, 500))
