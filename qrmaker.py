"""
    Copyright 2017 Daniel Harding

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
