print 'foo' == 'foo'
x = y = [1,2,3]
z = [1,2,3]
print x == y
print x == z
print x is y
print x is z

number = input( 'Enter your number: ') ### the scan function is input , not raw_input
print number
if 1 <= number <= 10:
	print 'Right!'
else:
	print 'Yeah!'

number = input( 'Enter your number: ') ### the scan function is input , not raw_input
print number
if 1 <= number and number <= 10:
	print 'Right!'
else:
	print 'Yeah!'