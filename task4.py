# Для всех серверов, параметры подключения
# к которым описаны в файле data/ssh_servers.txt.txt,
# вывести в консоль IP адрес(а) его шлюза/шлюзов

# 1. Прочитать параметры подключения к ssh серверам из файла
# 2. написать цикл, который последовательно подключается
# к каждому из серверов, используя эти параметры
# 3. Внутри этого цикла подать (в зависимости от типа операционной системы)
# команду и из ее теста вычленить интерeсующий нас адрес

with open("data/ssh_servers.txt") as f:
    text = f.read()
lines = text.split("\n")

for line in lines:
    params = line.split(";")
    # print(params)
    server = params[0]
    os_type = params[1]
    port = params[2]
    user = params[3]
    password = params[4]
    print(server, os_type, port, user, password)

