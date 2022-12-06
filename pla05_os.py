import os
import datetime

# os.system("CHCP 65001")
print(os.name)

# cmd = "calc"
# cmd = "dir"
# os.system(cmd)

# hosts = ["127.0.0.1", "ya.ru", "192.168.1.1", "bad.bad", "172.28.112.1"]

# for host in hosts:
#     cmd = f"ping {host}"
#     os.system(cmd)

# base = "172.28.112."
# for i in range(1, 10):
#     host = f"{base}{i}"
#     cmd = f"ping {host}"
#     os.system(cmd)

with open("data/hosts.txt") as f:
    hosts = f.read().split("\n")

for host in hosts:
    cmd = f"ping {host}"
    result = os.popen(cmd).read().encode("windows-1251").decode("866")
    # print("----------------------------------")
    # print(result)
    if result.find("TTL") > 0:
        # print(f"{host} is good")
        pass
    else:
        now = datetime.datetime.now()
        print(f"{now}\t{host} is BAD")
        with open("data/log.txt", "a", encoding="utf-8") as f:
            f.write(f"{now}\t{host} is BAD\n")
