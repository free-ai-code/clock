import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
