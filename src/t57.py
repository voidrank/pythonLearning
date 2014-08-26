class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self):
		super(Rectangle, self).__init__()
		self.width = 0
		self.height = 0
	def size():
	    doc = "The size property."
	    def fget(self):
	        return self.width, self.height
	    def fset(self, value):
	        self.width, self.height = value
	    def fdel(self):
	        pass
	    return locals()
	size = property(**size())

a = Rectangle()
a.size = (150,100)
print a.size