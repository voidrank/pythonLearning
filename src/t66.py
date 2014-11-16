class A(object):
	def __init__(self):
		super(A, self).__init__()

	def __enter__(self):
		return "Hope you Fe"
	
	def __exit__(self, type, value, traceback):
		pass

with A() as f:
	print f
