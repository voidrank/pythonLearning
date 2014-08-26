def hello_1(greeting, name):
	print '%s, %s' % (greeting, name)
def hello_2(name, greeting):
	print '%s, %s' % (name,greeting)

hello_2(name = 'world', greeting = 'hello')

def hello_3(greeting = 'hello', name = 'world'):
	print '%s, %s' % (greeting,name)

hello_3()
hello_3('hi')
hello_3('hi', ' ')
hello_3(name = '~')


def print_params( *params ):
	print params

print_params( 1, 2, 3, 4 )

def print_params_2( **params ):
	print params

print_params_2( x = 1, y = 1, z = 1 )

def print_params_3( **params ):
	for num in params:
		print params[num]

print_params_3( x=1, y=1, r=1 )