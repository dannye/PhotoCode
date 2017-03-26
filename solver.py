def solveMaze(t, m, s):
	import main
	if main.wallInFront(t, m):
		main.turnRight(t)
	if main.wallInFront(t, m):
		main.turnRight(t)
		main.turnRight(t)
	else:
		main.moveForward(t, m, s)

