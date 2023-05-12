from os import system, name, startfile

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start(app):
    system(f'start cmd /K "color B && python {app}"')