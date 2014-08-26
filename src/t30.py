scope = {}
scope['x'] = 2
scope['y'] = 3
print eval('x * y',scope)

scope1 = {}
exec 'x = 1' in scope1
exec 'y = 1' in scope1
print eval('x * y',scope1)
