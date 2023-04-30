
def layers(board):
    max_num = len(max(board.make_stacks_list())) + 1
    for j in range(1, max_num + 1):
        layer = " "
        i = 11
        for _ in range(0, 12):
            place = board.make_stacks_list()[i]
            if len(place) >= j:
                layer += (" " + place[0] + " ")
            else:
                layer += "   "
            i -= 1
        print(f"|{layer}|")
    for k in range(1, max_num):
        layer = " "
        for l in range(12, 24):
            place = board.make_stacks_list()[l]
            if len(place) >= k:
                layer += (" " + place[0] + " ")
            else:
                layer += "   "
        print(f"|{layer}|")

