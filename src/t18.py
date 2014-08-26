people = {
		
	'Alice':{
		'phone': '2431',
		'addr': 'Foo drive 23'
	},

	'Beth': {
		'phone': '9102',
		'addr': 'Foo street 42'
	},

	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}

}

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

name = raw_input('Name: ')

request = raw_input('phpne number(p) or address(a)?')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people: print "%s's %s is %s" %\
	(name, labels[key], people[name][key])

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<hl>%(title)s</hl>
<p>%(text)s</p>
</body> '''
data = { 'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data