from os import system, name, startfile

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start(app):
    if name == 'nt':
        system(f'start cmd /K "color B && python {app}"')

def set_background(color):
    if name == 'nt':
        system(f'color {color}')