class C(object):
	def __get__(self, instance, owner):
		print ("__get__() is called", instance, owner)

c = C()
c.a = 1
print(c.a)
