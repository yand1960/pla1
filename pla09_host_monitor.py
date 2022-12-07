import os
from datetime import datetime as dt
import time

def host_is_healthy(host):
    if os.name.find("nt") >= 0:
        cmd = f"ping {host}"

    if os.name.find("posix") >= 0:
        cmd = f"ping {host} -c 1"
    result = os.popen(cmd).read().encode("windows-1251").decode("866")

    return result.upper().find("TTL") > 0

def check_hosts(hosts, log_file):
    for host in hosts:
        if host_is_healthy(host):
            pass
        else:
            print(f"{dt.now()}\t{host} is BAD")
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{dt.now()}\t{host} is BAD\n")


if __name__ == "__main__":

    with open("data/hosts.txt") as f:
        hosts = f.read().split("\n")

    while True:
        try:
            check_hosts(hosts, "data/log1.txt")
        except Exception as e:
            with open("data/log2.txt", "a", encoding="utf-8") as f:
                print(f"{dt.now()}\t Cбой прогаммы\n{e} ")
                f.write(f"{dt.now()}\t Cбой прогаммы\n{e} \n")
        time.sleep(10)

