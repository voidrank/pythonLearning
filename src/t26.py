x = 1
while x <= 100:
	print x
	x += 1

words = ['this','is','an','ex','parrot']
for word in words:
	print word

for i in range(1,2):
	print i

d = { 'x': 1, 'y': 2, 'z': 3 }	
for key, value in d.items():
	print key, 'corresponds to', value 

names = ['anne','beth','george','damon']
ages = [12,45,32,102]

for i in range(len(names)):
	print names[i], 'is', ages[i], 'years old'

for name, age in zip(names,ages):
	print name, 'is', age, 'years old'

for i, s in enumerate(names):
	print i, 'is', s 

'''
	continue
	break
'''

from math import sqrt
for n in range (99,81,-1):
	root = sqrt(n)
	if root == int(root):
		print n
		break
else:
	print 'Didn\'t find it!'

print [ x*x for x in range(10) ]
print [ x*x for x in range(10) if x%3 == 0 ]
girls = ['aa','bb','cc']
boys = ['a','b','c']
print [b+'+'+g for b in boys for g in girls if b[0] == g[0]]