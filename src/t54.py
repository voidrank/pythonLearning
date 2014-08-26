def checkIndex(key):

	if not isinstance(key, (int, long)): raise TypeError
	if key<0: raise IndexError

class ArithmeticSequence:
	def __init__(self, start=0, step=1):

		self.start = start
		self.step = step
		self.changed = {}
	def __getitem__(self, key):

		checkIndex(key)
		try:
			return self.changed[key]
		except KeyError, e:
			return self.start + key*self.step
		else:
			pass
		finally:
			pass
	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value
	def __delitem__(self, key):
		checkIndex(key)
		del self.changed[key]

s = ArithmeticSequence(1, 2)
print s[4]
s[4] = 2
print s[5]

try:
	del s[4]
except Exception, e:
	print e
else:
	pass
finally:
	pass