import qrcode

keywords = [
    ["0", "0"],
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"],
    ["IF", "if"],
    ["ELSE", "else"],
    ["WHILE", "while"],
    ["START", "start"],
    ["END", "end"],
    ["+", "plus"],
    ["-", "minus"],
    ["*", "multiply"],
    ["/", "divide"],
    ["%", "mod"],
    ["<", ""], "less_than"],
    [">", "greater_than"],
    ["=", "equal"],
    ["NOT", "not"],
    ["AND", "and"],
    ["OR", "or"],
    ["MOVE_FORWARD", "move_forward"],
    ["TURN_LEFT", "turn_left"],
    ["TURN_RIGHT", "turn_right"],
    ["WALL_IN_FRONT", "wall_in_front"],
    ["VAR_1", "var_1"],
    ["VAR_2", "var_2"],
    ["VAR_3", "var_3"],
    ["VAR_4", "var_4"],
    ["VAR_5", "var_5"]
    ]

for i, keyword in enumerate(keywords):
    img = qrcode.make(keyword[0])
    print (keyword[1])
    img.save("keywords/" + keyword[1] + ".png")
