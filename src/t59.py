class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self):
		super(Rectangle, self).__init__()
	def __setattr__(self, name, value):
		if name == 'size':
			self.width, self.height = value
		else:
			self.__dict__[name] = value
	def __getattr__(self, name):
		if name == 'size':
			return self.width, self.height
		else:
			raise AttributeError

a = Rectangle()
a.size = (150,100)
print a.size
print a.s