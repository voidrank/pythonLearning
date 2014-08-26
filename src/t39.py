class Person:
	address = ''

	def setName(self,name):
		self.name = name

	def setSex(self,Sex):
		self.Sex = Sex

	def getName(self):
		return self.name

	def greet(self):
		print "Hello,world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anak in Skywalker')
foo.greet()
bar.greet()

bar.Sex = 'man'
bar.address = 'h13'