import os
import datetime
import time

def host_is_healthy(host):

    if os.name.find("nt") >= 0:
        cmd = f"ping {host}"

    if os.name.find("posix") >= 0:
        cmd = f"ping {host} -c 1"

    result = os.popen(cmd).read().encode("windows-1251").decode("866")

    return result.upper().find("TTL") > 0

def check_hosts(hosts):



with open("data/hosts.txt") as f:
    hosts = f.read().split("\n")


while True:

    for host in hosts:
        if os.name.find("nt") >= 0:
            cmd = f"ping {host}"

        if os.name.find("posix") >= 0:
            cmd = f"ping {host} -c 1"

        result = os.popen(cmd).read().encode("windows-1251").decode("866")

        if result.upper().find("TTL") > 0:
            # print(f"{host} is good")
            pass
        else:
            now = datetime.datetime.now()
            print(f"{now}\t{host} is BAD")
            with open("data/log.txt", "a", encoding="utf-8") as f:
                f.write(f"{now}\t{host} is BAD\n")

    time.sleep(10)
