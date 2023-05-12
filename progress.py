from time import sleep
from os_comands import clear

while True:
    with open("progress.txt", "r") as file:
        clear()
        data = file.read()
        print(data)
        sleep(1)
