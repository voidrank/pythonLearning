class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

##issubclasss(SPAMFilter,Filter)
print hasattr(Filter,'init')
print hasattr(Filter,'talk')
