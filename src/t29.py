from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
exec 'print sqrt' in scope
print sqrt(4)
print scope.keys()

print eval(raw_input()) 
'''
	x = 0
	input(x)
	print x
'''