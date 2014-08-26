from string import Template
s = Template('The radium is $x')
print s.substitute(x='1')

s = Template('The radium is $$${x}')
print s.substitute(x='1')

s = Template('The radium is ii$x${y}xx')
d = {}
d['x'] = '1'
d['y'] = '2'
print s.substitute(d)
