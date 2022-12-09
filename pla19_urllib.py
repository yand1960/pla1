from urllib import request
import re

url = "http://cbr.ru"
with request.urlopen(url) as req:
    result = req.read().decode("utf-8")
# print(result)

# Найдите курс доллара в result с помощью регулярного выражения (13:57)
# pattern = '_right mono-num">(\d+,\d+) ₽'
#? - нежадный поиск
pattern = 'USD,[\s\S]+?_right mono-num">(\d+,\d+) ₽'
rates = re.findall(pattern, result)
print(rates[0])
