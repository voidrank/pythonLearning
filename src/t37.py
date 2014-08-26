x = 1
scope = vars()
print scope['x']
scope['x'] += 1
print x

'it seems very interesting!!'

def combine(parameter):
	print parameter + external

external = 'berry'
combine('Shrub')

x = 1
def change_global():
	global x
	x = x + 1
print x

parameter = 'berry'
def combine_2(parameter):
	parameter = 'strew'
	print parameter + globals()['parameter']

change_global()
combine_2('')