# Прочитать из текстового файла - не проблема
f = open("data/amounts.txt", "r")
text = f.read()
# print(text)
f.close()

# Пример записи в файл:
# f = open("data/results.txt", "w")
# f.write("hello, world\ngood bye, world")
# f.close()

# Далее надо разобрать это текст для дальнейшей обработки
amounts = text.split("\n")
print(amounts)

# Обрабатываем разобранные данные
# В данном случае - находим среди них "нормальные" данные
# и записываем их в файл results.txt

f = open("data/results.txt", "w")

for x in amounts:
    # print(f"число {x}")
    amount = int(x) #  конверсия типа от str к int
    if amount >= 10 and amount < 100:
        print(f"Нормальное число {amount}")
        f.write(str(amount) + "; ")

f.close()

# ЗАДАЧА 1. Поставьте PyCharm в Linux, перенесите туда наши файлы
# и убедитесь, что там работают не хуже

# ЗАДАЧА 2. Напишите программный код, который из файла data/people.txt
# выведет в консоль фамилии сотрудников, которые начинаются на A



