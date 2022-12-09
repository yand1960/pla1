import time
from threading import Thread, Lock

lock = Lock()
results = []

def measure(n):
    time.sleep(3) # симуляция задержки
    result = 10 * n # симуляция измерения
    lock.acquire() # один из механизмов синхронизации
    # print(n, result)
    results.append([n, result])
    lock.release()
    return result

if __name__ == "__main__":

    # синхронный код прост, но плох, когда возникает задержка
    # for n in range(1, 10):
    #     result = measure(n)
    #     print(n, result)

    pool = []
    for n in range(1, 10):
        thread = Thread(target=measure, args=(n,))
        pool.append(thread)
        thread.start()

    # time.sleep(3.5) # дешево и сердито

    # while len(results) < 9:
    #     time.sleep(0.1)

    for thread in pool:
        thread.join() # ждем, пока поток закончит работу

    results.sort()
    # print(results)
    for measurement in results:
        print(f"Датчик {measurement[0]}: {measurement[1]}")
