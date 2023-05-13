from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start(app):
    if name == 'nt':
        system(f'start cmd /K "color B && python {app}"')
    else:
        system(f'gnome-terminal -- bash -c "python3 {app}"')
        system("osascript -e 'tell application"+'"Terminal"'+'to do script'+f'"python3 {app}"'+"'")

def set_background(color):
    if name == 'nt':
        system(f'color {color}')