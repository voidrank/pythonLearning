tag = '<a hreaf="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]

numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers[3:6]
print numbers[0:1]
print numbers[7:10]
print numbers[-3:-1]
print numbers[-3:0]
print numbers[-3:]

'''
url = raw_input('Please enter the URL ')
domain = url[11:-4]
print "Domain name " + domain
'''

print numbers[0:10:1]
print numbers[8:3:-1]
print numbers[10:0:-2]
print numbers[::-2]
print numbers[5::-2]
print numbers[:5:-2]

numbers = numbers + numbers
print numbers[:]
numbers = 2*numbers
print numbers[:]

