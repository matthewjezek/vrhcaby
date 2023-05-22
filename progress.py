from time import sleep
import os_comands as os
import json
import colorama
from colorama import Fore, Back, Style


def show_data():
    with open('progress.txt', 'r') as file:
        colorama.init()
        lines = file.readlines()
        if "KILL" in lines[-1]:
            print(Fore.LIGHTRED_EX + lines[-1])
        elif "SAVE" in lines[-1]:
            print(Fore.GREEN + lines[-1])
        elif "END" in lines[-1]:
            print(Fore.YELLOW + lines[-1])
        elif "move" in lines[-1]:
            print(Fore.WHITE + lines[-1])


def check_change():
    print("PROGRESS:\n---------------------\n")
    while True:
        with open("progress.txt", "r") as file:
            data_1 = file.read()
            sleep(0.1)
        with open("progress.txt", "r") as file:
            data_2 = file.read()
        if data_1 != data_2:
            show_data()
        with open('exit.json', 'r') as f:
            exit_app = json.load(f)
        if exit_app:
            os.kill_window()


exit_app = False
check_change()
