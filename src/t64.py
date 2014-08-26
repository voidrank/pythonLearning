def flatten(nested):
	try:
		try:
			nested + ''
		except TypeError:
			pass
		else:
			raise TypeError
		for i in nested:
			for j in flatten(i):
				yield j
	except TypeError:
		yield nested

nested = ['1123',[1,2,1],[[1,2],1],1]
print list(flatten(nested))