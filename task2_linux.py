# Напишите код, который обработает результат выполнения
# команды ipconfig (ifconfig или какой-то другой, на ваш выбор)
# и выдаст первый адрес  IP адрес текущего компа

import os
import re

cmd = f"ifconfig"
result = os.popen(cmd).read().encode("windows-1251").decode("866")

# print(result)

# \. - просто точка, . - любой символ
# [\.\s] - или точка или пробельный символ, + - в любом количестве от 1
# () - группа, интересующая в качестве результата
pattern = "\n\s+inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
results = re.findall(pattern, result)
print(results)

