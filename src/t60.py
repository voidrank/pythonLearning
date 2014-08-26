class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		super(Fib, self).__init__()
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a+self.b
		return self.a
	def __iter__(self):
		return self

fibs = Fib()
for f in fibs:
	print f
	if f > 1000:
		break