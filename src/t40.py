class Secretive(object):
	"""docstring for Secretive"""
	def __inacessible(self):
		print "But you can't see me"
	def accessible(self):
		print "The secret message is:"
		self.__inacessible()

s = Secretive()
s.accessible()
s._Secretive__inaccessible()