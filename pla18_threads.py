import time
from threading import Thread, Lock

lock = Lock()
results = []

def measure(n):
    time.sleep(3) # симуляция задержки
    result = 10 * n # симуляция измерения
    lock.acquire() # один из механизмов синхронизации
    # print(n, result)
    results.append(result)
    lock.release()
    return result

if __name__ == "__main__":

    # синхронный код прост, но плох, когда возникает задержка
    # for n in range(1, 10):
    #     result = measure(n)
    #     print(n, result)

    for n in range(1, 10):
        thread = Thread(target=measure, args=(n,))
        thread.start()

    print(results)
