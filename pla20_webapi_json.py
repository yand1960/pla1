from urllib import request
import json

url = "http://www.cbr-xml-daily.ru/daily_json.js"
with request.urlopen(url) as req:
    result = req.read().decode("utf-8")
# print(result)

rates = json.loads(result)
print(rates['Valute']['USD']['Value'])

# Одной строкой кода выведите курс USD (14:34)

