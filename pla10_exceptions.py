data1 = [1000, 2000, 3000, 4000, "qwerty", 6000]
data2 = [10, 20, 30, 0, 0, 777]

for i in range(0, len(data1)):
    try:
        x = data1[i]
        y = data2[i]
        z = x / y
        print(f"{x}:{y}={z}")
    except ZeroDivisionError:
        z = 999999
        print(f"{x}:{y}={z}")
    except Exception as e:
        # не проглатывайте ошибку - это антипаттерн
        # pass
        print(f"Произошла ошибка при обработке данных номер {i + 1} ")
        print(f"Детали ошибки: {e}")

print("И делается что-то еще...")