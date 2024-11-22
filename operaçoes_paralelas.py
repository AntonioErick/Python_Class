import time
import threading



start_time = time.time()
threads = []

def contador(numero):
    for i in range(numero):
        print(i)

for valor in range(5):
    t = threading.Thread(target=contador,args=(100000,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print(time.time() - start_time)