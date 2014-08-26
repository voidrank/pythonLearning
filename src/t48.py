def describePerson(person):
	print 'Description of', person['name']
	print 'Age:', person['age']
	try:
		print 'Occuption: ' + person['occupation']
	except KeyError:
		pass

person = { 'name':'Adam', 'age':'18'}
describePerson(person)