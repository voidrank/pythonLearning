names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
numbers = ['2345','9102','3158','0142','5551']
print numbers[names.index('Alice')]

phonebook = { 'Alice':'1234', 'Beth':'3244', 'Cecil':'3158' }
print phonebook['Alice']

items = [('name', 'Gumby'),('age','42')]
d = dict(items)
print d
print d['name']

print len(phonebook)
d['kk'] = 1
print d
del d['kk']
print d
print 'age' in d