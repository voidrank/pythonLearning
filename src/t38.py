import bisect
import random

random.seed(1)
print 'new pos contents'
print '----------------'
seq = []

for i in range(1,15):
	x = random.randint(1,100)
	pos = bisect.bisect(seq,x)
	bisect.insort(seq,x)
	print '%3d %3d'%(x,pos),seq
'bisect----------------'

def func(x):
	return x.isalnum()

seq = ["foo","x41",'?!','***']
print filter(func,seq)

print filter(lambda x: x.isalnum(), seq)

print reduce(lambda x, y: x+y, seq)