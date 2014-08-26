class Bird:
	def __init__(self):
		self.hungry = 1
	def eat(self):
		if self.hungry:
			print 'Aaaaa'
			self.hungry = 0
		else:
			'thank you'

class SongBird(Bird):
	def __init__(self):
		Bird.__init__(self)
		self.sound = 'squawk!'
	def sing(self):
		print self.sound

a = Bird()
a.eat()
a.eat()
b = SongBird()
b.eat()