seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq)

dirs = '', 'usr', 'bin', 'env'
print 'C:'+'\\'.join(dirs)

dirs = ['abc','voidrank','cookie']
if 'ABC'.lower() in dirs: print 'Found it!'

print "I'm here with her".replace("I'm here","You are there")
print '1+2+3+4-5'.split('+','-')