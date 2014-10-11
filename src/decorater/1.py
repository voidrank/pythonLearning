def de(f):
	def _call_():
		print"-----------"
		return f()
	return _call_


def func1():
	print "I am function func1"

@de
def func2():
	print "I am function func2"

func1 = de(func1)


func1()
func2()
