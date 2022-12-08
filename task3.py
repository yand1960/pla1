# Написать программный код, который покажет пользователю в экселе
# все товары, цена которых в диапазоне от 100 до 1000

import pymssql
import os
from _datetime import datetime as dt

with pymssql.connect(
    server="yand.dyndns.org",
    database="AdventureWorks",
    user="northwind",
    password="northwind"
) as conn:

    sql = "SELECT ProductID, Name, ProductNumber, ListPrice FROM Production.Product"

    cursor = conn.cursor()
    cursor.execute(sql)

    products = cursor.fetchall()

file_name = f"products_{dt.now()}.csv"
file_name = file_name.replace(":", "_")
file_name = file_name.replace(" ", "_")

print(file_name)

with open(f"data/{file_name}", "w") as f:
    f.write("ID;Название;Артикул;Цена\n")
    for p in products:
        print(f"{p[1]:40}\t\t{p[3]}")
        f.write(f"{p[0]};{p[1]};{p[2]};{p[3]}\n")

os.system(f"start Excel data\\{file_name}")