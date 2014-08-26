__metaclass__ = type
class Bird():
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Aaaah...'
			hungry = False
		else:
			print 'No, thanks!'
class SongBird(Bird):
	def __init__(self):
		super(SongBird, self).__init__()
		self.sound = 'Squawk!'
	def sing(self):
		print self.sound

a = SongBird()
a.sing()