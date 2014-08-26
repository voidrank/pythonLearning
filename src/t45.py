while True:
	try:
		x = input()
		y = input()
		value = x/y
		print 'the value is', value
	except Exception,e:
		print 'Invalid input:' ,e
		print 'Please try again'
	else:
		break