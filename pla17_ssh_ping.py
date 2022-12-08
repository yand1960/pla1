from paramiko import SSHClient
import paramiko

hosts = ["127.0.0.1", "ya.ru",  "bad.bad", "172.24.224.1"]

with SSHClient() as client:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(
        hostname="172.24.236.10",
        port=22,
        username="yand",
        password="Pa$$w0rd"
    )

    for host in hosts:
        print("------------------------------------------------------")
        cmd = f"ping {host} -c 1"
        result = client.exec_command(cmd)[1].read().decode("UTF-8")
        # print(result)
        if result.upper().find("TTL") > 0:
            print(f"{host} is good")
        else:
            print(f"{host} is BAD")