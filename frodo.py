keywords = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "IF",
    "ELSE",
    "WHILE",
    "START",
    "END",
    "+",
    "-",
    "*",
    "/",
    "%",
    "<",
    ">",
    "=",
    "NOT",
    "AND",
    "OR",
    "MOVE_FORWARD",
    "TURN_LEFT",
    "TURN_RIGHT",
    "WALL_IN_FRONT",
    "VAR_1",
    "VAR_2",
    "VAR_3",
    "VAR_4",
    "VAR_5"
    ]

numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
    ]

operators = [
    "+",
    "-",
    "*",
    "/",
    "%",
    "<",
    ">",
    "="
    ]

variables = [
    "VAR_1",
    "VAR_2",
    "VAR_3",
    "VAR_4",
    "VAR_5"
    ]

actions = [
    "MOVE_FORWARD",
    "TURN_LEFT",
    "TURN_RIGHT",
    "WALL_IN_FRONT"
    ]

def parseFrodo(filename):
    frodo = open(filename, 'r')
    indent = 1
    output = 'def solveMaze(t, m, s):\n\timport main\n'
    inIfOrWhile = False
    rightSide = False
    printingNumber = False
    printingOperator = False
    beginningOfLine = True
    lastkeyword = ''
    for keyword in frodo:
        keyword = keyword.rstrip('\r\n')
        #print "keyword: " + keyword
        if keyword not in keywords:
            output = ''
            #print "bad keyword:" + keyword
            break
        
        if beginningOfLine and keyword != "END":
            if keyword == "ELSE":
                indent -= 1
            for i in range(0, indent):
                output += '\t'
            beginningOfLine = False
        
        if keyword in numbers and lastkeyword in numbers:
            output += keyword
        
        if keyword in operators and lastkeyword in operators:
            output += keyword
        
        if rightSide and not(keyword in numbers and lastkeyword in numbers) and keyword != "START" and keyword != "END":
            output += "\n"
            beginningOfLine = True
        
        if keyword not in numbers and printingNumber:
            printingNumber = False
            if not rightSide:
                output += ' '
        
        if keyword not in operators and printingOperator:
            printingOperator = False
            rightSide = True
            output += ' '
        
        if keyword in operators and not printingOperator:
            printingOperator = True
            output += keyword
        
        if keyword in numbers and not printingNumber:
            printingNumber = True
            output += keyword
        
        if keyword in variables:
            if keyword == "VAR_1":
                output += "var1 "
            if keyword == "VAR_2":
                output += "var2 "
            if keyword == "VAR_3":
                output += "var3 "
            if keyword == "VAR_4":
                output += "var4 "
            if keyword == "VAR_5":
                output += "var5 "
        
        if keyword in actions:
            if keyword == "MOVE_FORWARD":
                output += "main.moveForward(t, m, s)\n"
                beginningOfLine = True
            if keyword == "TURN_LEFT":
                output += "main.turnLeft(t)\n"
                beginningOfLine = True
            if keyword == "TURN_RIGHT":
                output += "main.turnRight(t)\n"
                beginningOfLine = True
            if keyword == "WALL_IN_FRONT":
                output += "main.wallInFront(t, m)"
        
        if keyword == "IF":
            output += "if "
            inIfOrWhile = True
        if keyword == "ELSE":
            output += "else:\n"
            indent += 1
            beginningOfLine = True
        if keyword == "WHILE":
            output += "while "
            inIfOrWhile = True
        if keyword == "START":
            output += ":\n"
            indent += 1
            beginningOfLine = True
        if keyword == "END":
            indent -= 1
        if keyword == "NOT":
            output += "not "
        if keyword == "AND":
            output += "and "
        if keyword == "OR":
            output += "or "
        
        if indent == 0:
            output = ''
            break
        
        lastkeyword = keyword
    #print output
    #print indent
    outfile  = open("solver.py", 'w')
    outfile.write(output + '\n')

"""
if __name__ == '__main__':
    parseFrodo("script.frodo")
"""
