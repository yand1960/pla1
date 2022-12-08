from paramiko import SSHClient
import paramiko

with SSHClient() as client:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(
        hostname="yand.dyndns.org",
        port=16622,
        username="sshuser",
        password="unkququmumulala789"
    )

    # 1. Ввыполнение команд на удаленном сервере

    cmd = "dir"
    # [1] - это выходной поток команды,
    # [0] - это входной поток команды,
    # [2] - это поток вывода ошибок,
    result = client.exec_command(cmd)[1].read().decode("866")
    print(result)

    # 2. Действия с файлами по sftp
    with client.open_sftp() as ftp:
        # 2.1 Получаем файл с целевого хоста
        ftp.chdir("c:\\tmp") # на целевом хосте
        ftp.get("config.txt", "data\\config.txt")
        # 2.2 Редактируем это файл
        text = "I am Yuri Andienko from ssh client"
        with open("data/config.txt", "w") as f:
            f.write(text)
        # 2.3 Копируем измененный файл на целевой хост
        ftp.put("data\\config.txt", "YA_config.txt")

