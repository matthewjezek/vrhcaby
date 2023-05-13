from time import sleep
import os_comands as os

def show_data():
    with open("progress.txt", "r") as file:
        data = file.read()
        os.clear()
        print(data)

def check_change():
    show_data()
    while True:
        with open("progress.txt", "r") as file:
            data_1 = file.read()
            sleep(0.1)
        with open("progress.txt", "r") as file:
            data_2 = file.read()
        if data_1 != data_2:
            show_data()

check_change()