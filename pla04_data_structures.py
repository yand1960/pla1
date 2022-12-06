# список списков

people = [
    ["Andrienko", "Yuri", 123456],
    ["Pupkin", "Vasya", 77777],
    ["Andreev", "Andrey", 300000]
]

# print(people)

for person in people:
    print(f"{person[1]} {person[0]} has salary {person[2]}")
print("---------------------------------------------------")

# Словари
person1 =  {"lastName": "Andrienko", "firstName": "Yuri", "salary": 123456}
print(f"{person1['lastName']} {person1['firstName']} has salary {person1['salary']}")
print("---------------------------------------------------")

# Список словарей
people = [
    {
        "lastName": "Andrienko",
        "firstName": "Yuri",
        "salary": 123456},

    {"lastName": "Pupkun", "firstName": "Vasya", "salary": 77777},
    {"lastName": "Andrey", "firstName": "Andreev", "salary": 300000}
]

for p in people:
    print(f"{p['lastName']}\t {p['firstName']}\t has salary\t{p['salary']}")