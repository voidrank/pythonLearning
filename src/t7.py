print list('hello')

x = [1,1,1]
x[1] = 2
print x

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Eael']
del names[2]
print names

name = list('Perl')
name[1:] = list('ython')
print name

numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers
numbers[1:4] = []
print numbers

lst = [1,2,3]
lst.append(1)
print lst

lst.append(lst.pop())
