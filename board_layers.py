
def layers(board): # Dynamický tisk po vstvách podle obsahu vrcholů
    max_num = 5
    for i in range(0, 24):
        if len(board.stacks[i]) > max_num:
            max_num = len(board.stacks[i])
    for i in range(0, max_num):
        layer = " "
        for j in range(11, -1, -1):
            place = board.stacks[j]
            if len(place) >= i+1:
                layer += (" " + place[i].color + " ")
            else:
                layer += "   "
        print(f"|{layer}|")
    print("|                                     |")
    for i in range(max_num, -1, -1):
        layer = " "
        for j in range(12, 24):
            place = board.stacks[j]
            if len(place) >= i+1:
                layer += (" " + place[i].color + " ")
            else:
                layer += "   "
        print(f"|{layer}|")

