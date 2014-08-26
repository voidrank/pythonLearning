def hello(name):
	return 'hello, ' + name + '!'

print hello('world')
print hello('Gumby')

def fibs(num):
	result = [0, 1]
	for i in range(num-2):
		result.append(result[-1] + result[-2])
	return result

print fibs(3)