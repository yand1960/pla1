# Напишите код, который обработает результат выполнения
# команды ipconfig (ifconfig или какой-то другой, на ваш выбор)
# и выдаст первый адрес  IP адрес текущего компа

import os
import re

cmd = f"ipconfig"
result = os.popen(cmd).read().encode("windows-1251").decode("866")

# print(result)

# \. - просто точка, . - любой символ
# [\.\s] - или точка или пробельный символ, + - в любом количестве от 1
# () - группа, интересующая в качестве результата
# pattern = "\n\s+IPv4 Address[\.\s]+ : \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern = "\n\s+IPv4 Address[\.\s]+ : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
results = re.findall(pattern, result)
print(results[0])

# Рабочий способ, но не мастерский
# result = results[0]
# pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# results = re.findall(pattern, result)
# print(results[0])

# Получить маску подсети
pattern = "\n\s+Default Gateway[\.\s]+ : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
results = re.findall(pattern, result)
print(results[0])