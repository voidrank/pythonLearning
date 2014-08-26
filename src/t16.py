from string import maketrans
table = maketrans('cs','kz')
print len(table)
print 'this is an incredible test'.translate(table,' ')

