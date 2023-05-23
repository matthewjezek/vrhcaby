from time import sleep
import os_comands as os
import json
import colorama as cl


def set_color(line, move_type):
    cl.init()
    match move_type:
        case "KILL":
            line = cl.Fore.LIGHTRED_EX + line
        case "SAVE":
            line = cl.Fore.GREEN + line
        case "END":
            line = cl.Fore.YELLOW + line
        case "move":
            line = cl.Fore.WHITE + line
    return line


def show_data():
    print("PROGRESS:\n---------------------\n")
    with open('progress.json', 'r') as file:
        data = json.load(file)
    for index in range(0, len(data)):
        line = data[index]
        player_name = line[0]
        option = line[1]
        line = "\n" if index > 0 and data[index - 1][0] != player_name else ""
        line += f"{player_name}: {option[0]} -> {option[1]}, [{option[2]}] - {option[3]}"
        line = set_color(line, option[3])
        print(line)


def show_last_line():
    with open('progress.json', 'r') as file:
        data = json.load(file)
        line = data[-1]
        player_name = line[0]
        option = line[1]
        line = "\n" if len(data) > 1 and player_name != data[-2][0] else ""
        line += f"{player_name}: {option[0]} -> {option[1]}, [{option[2]}] - {option[3]}"
        line = set_color(line, option[3])
        print(line)


def check_exit():
    with open('exit.json', 'r') as f:
        status = json.load(f)
    return True if status else False


def check_change():
    with open("progress.json", "r") as file:
        data_1 = json.load(file)
        sleep(1)
    with open("progress.json", "r") as file:
        data_2 = json.load(file)
    return True if data_1 != data_2 else False


show_data()
while not check_exit():
    if check_change():
        show_last_line()
os.kill_window()
