# Для всех серверов, параметры подключения
# к которым описаны в файле data/ssh_servers.txt.txt,
# вывести в консоль IP адрес(а) его шлюза/шлюзов

# 1. Прочитать параметры подключения к ssh серверам из файла
# 2. написать цикл, который последовательно подключается
# к каждому из серверов, используя эти параметры
# 3. Внутри этого цикла подать (в зависимости от типа операционной системы)
# команду и из текста результата ее выполнения вычленить интерeсующий нас адрес

from paramiko import SSHClient
import paramiko
import re

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
    # print(server, os_type, port, user, password)

    try:
        with SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(
                hostname=server,
                port=port,
                username=user,
                password=password
            )

            if os_type == "linux":
                cmd = "ip r"
                result = client.exec_command(cmd)[1].read().decode("866")
                # print(result)
                pattern = "default via (\d{0,3}\.\d{0,3}\.\d{0,3}.\d{0,3})"
                gateways = re.findall(pattern, result)
                print(f"host: {server} gateway: {gateways[0]}")

    except Exception as e:
        print(f"host: {server} ERROR: {e}")





