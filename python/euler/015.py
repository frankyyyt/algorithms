grid = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
current_location = [0, 0]
target_location = [2, 2]

routes = []
route = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]
routes.append(route)

def path_finder(x, y):
	print x, y
	if x == 2 and y == 2:
		print "path complete"
	else:
		if y < 2:
			y += 1
			path_finder(x, y)
		elif x < 2:
			x += 1
			path_finder(x, y)
	return

def path_finder_two():
	switchover_number = 2
	while switchover_number >= 0:
		x = 0
		y = 0
		while x <= switchover_number:
			print x, y
			x += 1
		while y <= 2:
			print x, y
			y += 1
		switchover_number -= 1
		print "path complete"
	return

path_finder_two()
