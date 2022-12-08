# Написать программный код, который покажет пользователю в экселе
# все товары, цена которых в диапазоне от 100 до 1000

import pymssql
import os
from _datetime import datetime as dt
import sys

# Вариант 1 - параметрые вписываются в программу
# ************* Укажите необходимые параметры ***********
MIN_PRICE = 100
MAX_PRICE = 1000
# *****************************************************

# Вариант 2 - интерактивный запрос с помощью input
# MIN_PRICE = input("Введите минимальную цену: ")
# MAX_PRICE = input("Введите максимальную цену: ")

# Вариант 3 - параметры указываются в командной строке
if len(sys.orig_argv) >= 3:
    MIN_PRICE = sys.argv[1]
    MAX_PRICE = sys.argv[2]
else:
    print("Вы не ввели параметры в командной строке, использованы значения по умолчанию ")

with pymssql.connect(
    server="yand.dyndns.org",
    database="AdventureWorks",
    user="northwind",
    password="northwind"
) as conn:

    sql = f"""
        SELECT ProductID, Name, ProductNumber, ListPrice 
        FROM Production.Product
        WHERE ListPrice>{MIN_PRICE} AND ListPrice<{MAX_PRICE}
    """

    cursor = conn.cursor()
    cursor.execute(sql)

    products = cursor.fetchall()

file_name = f"products_{dt.now()}.csv"
file_name = file_name.replace(":", "_")
file_name = file_name.replace(" ", "_")

print(file_name)

with open(f"data/{file_name}", "w") as f:
    if len(products) > 0:
        f.write("ID;Название;Артикул;Цена\n")
        for p in products:
            print(f"{p[1]:40}\t\t{p[3]}")
            price = str(p[3]).replace(".",",")
            f.write(f"{p[0]};{p[1]};{p[2]};{price}\n")
    else:
        f.write("Товаров в указанном ценовом диапазоне не найдено\n")

os.system(f"start Excel data\\{file_name}")