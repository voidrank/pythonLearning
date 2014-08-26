nested = [[1,2], 1, [[1,2],1], 1]

def flatten(nested):
	try:
		for i in nested:
			for j in flatten(i):
				yield j
	except TypeError:
		yield nested

print list(flatten(nested))
