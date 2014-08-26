width = input('Please enter the width: ')

price_width = 10
item_width = width - price_width

header_format 	= '%-*s%*s'
format 			= '%-*s%*.2f'

print '=' * width 

print header_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format % (item_width, 'Apple', price_width, 0.4 )
print format % (item_width, 'Apple', price_width, 0.4 )
print format % (item_width, 'Apple', price_width, 0.4 )
print format % (item_width, 'Apple', price_width, 0.4 )
print format % (item_width, 'Apple', price_width, 0.4 )
print format % (item_width, 'Apple', price_width, 0.4 )
