def solveMaze(t, m, s):
	import main
	if main.wallInFront(t, m):
		main.turnLeft(t)
	else:
		main.moveForward(t, m, s)

