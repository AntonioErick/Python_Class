import os
import time
import threading


def pinger(site):
    os.system(f"ping {site}")

start_time = time.time()

urls = ["www.google.com","www.facebook.com","www.youtube.com"]
threads = []

for url in urls:
    t = threading.Thread(target=pinger, args=(url,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print(time.time() - start_time)