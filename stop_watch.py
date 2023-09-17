import time
import os
start = time.time()
print("timer began \n1s")
time.sleep(1)
print("2s")
time.sleep(1)
print("3s...")
print("press Ctrl + C to stop the timer")

i = 3
try:
    while True:
        print(f"{i}seconds")
        i += 1
        time.sleep(1)
except KeyboardInterrupt:
    end = time.time()
    timing = end-start
    print(f"\nDone... in {timing}")
