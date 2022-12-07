import pymssql

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

# print(products)

for p in products:
    print(f"{p[1]:40}\t\t{p[3]}")

