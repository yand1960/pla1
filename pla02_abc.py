# Конкатенция строк
s1 = "Yuri"
s2 = "Andrienko"
s3 = s1 + " " + s2
print(s3)
s4 = s2 + ", " + s1
print(s4)

# Имена переменных
first_name = "Yuri"
last_name = "Andrienko"
full_name = first_name + " " + last_name
print(full_name)
first_letter = first_name[0] # это называется срез
name_with_initial = first_letter + "." + last_name
print(name_with_initial)

# Разборка строки
full_name = "Yuri Andrienko"
space_index = full_name.index(" ")
# print(space_index)
first_name = full_name[0:space_index]
last_name = full_name[space_index + 1:]
# name2 = last_name + ", " + first_name
# print(name2)

# f - строка
otchestvo = "Anatolievich"
# name2 = last_name + ", " + first_name + " " + otchestvo
name2 = f"{last_name}, {first_name} {otchestvo}"
print(name2)

# Вывести что-ьто типа Y.A.Anatolievich (14:10)
name3 = f"{first_name[0]}.{otchestvo[0]}.{last_name}"
print(name3)

#  Ветвление (условный оператор)
amount = 1

if amount < 10:
    print("Маловато будет!")
    print("Овес нынче дорог")

if amount  >= 10 and amount < 100:
    print("Нормально! Спасибо")

if amount >= 100:
    print("Премного благодарен!")
    print("Приходите еще")

# print("Анализ завершен!")

# Циклы и списки
amounts = [12, 123, 1, 77, 7, 777]
amounts.append(8)
print(amounts[1])
print(amounts)

for x in amounts:
    print(f"Анализируем сумму {x}...")

    if x < 10:
        print("Маловато будет!")
        print("Овес нынче дорог")

    if x >= 10 and x < 100:
        print("Нормально! Спасибо")

    if x >= 100:
        print("Премного благодарен!")
        print("Приходите еще")

print("Анализ завершен!")
