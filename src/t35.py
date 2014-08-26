def change(n):
	n = 'love'

x = 'hate'
change(x)
print x

def change_a(n):
	n[0] = 'Mr. Gumby'

names = [ 'Mrs Entity', 'Mrs. Thing']
change_a(names)
print names

n = names[:]
print n is names
print n == names
names[0] = ''
print names
print n