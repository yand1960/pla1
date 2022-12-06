# ЗАДАЧА 0. Поставьте PyCharm в Linux, перенесите туда наши файлы
# и убедитесь, что там они работают не хуже

# ЗАДАЧА 1. Напишите программный код, который из файла data/people.txt
# выведет в консоль фамилии сотрудников, которые начинаются на A

f = open("data/people.txt", encoding="utf-8")
text = f.read()
f.close()

# Далее надо разобрать это текст для дальнейшей обработки
people = text.split("\n")
print(people)

# for person in people:
#     if person.startswith("А"):
#         print(person)

# Что если нужно вывести в формате Юрий Андриенко
for person in people:

    splitted = person.split(", ")
    # print(splitted)
    first_name = splitted[1]
    last_name = splitted[0]

    if person.startswith("А"):
        print(f"{first_name} {last_name}")
