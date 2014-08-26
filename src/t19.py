d = {} 
d['name'] = 'Gumby'
d['age'] = '42'
print d
returned_value = d.clear()
print returned_value

x = {}
y = x
x['key'] = 'value'
print y

x = y.copy()
y.clear()
print x
print y

x = { 'username': 'admin', 'machine': {'foo', 'bar', 'baz'}}
y = x.copy()
y['machine'].remove('bar') 
print y
print x

from copy import deepcopy

x = { 'username': 'admin', 'machine': {'foo', 'bar', 'baz'}}
y = deepcopy(x)
y['machine'].remove('bar') 
print y
print x

t = {}
t.fromkeys(['name','age'])
t = {}.fromkeys(['name','age'],'(unknown)')
print t
print t.get('name')
print t.get('age')
print t.get('address')
print t.get('address','N/A')
t = {}
print t.setdefault('address','none')
print t

print t.values()