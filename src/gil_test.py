import time
from threading import Thread


def add(target: int):
    while target > 0:
        target -= 1


target: int = 1_000_000_000
t1: Thread = Thread(target=add, args=[target // 2, ])
t2: Thread = Thread(target=add, args=[target // 2, ])

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

