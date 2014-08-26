greeting = 'Hello'
print greeting[0]

months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December',
]

endings = [ 'st', 'nd', 'rd' ] + 17 * ['th'] \
			+ [ 'st', 'nd', 'rd' ] + 7 * ['th'] \
			+ [ 'it' ]

year = raw_input("year ")
month = raw_input("month ")
day = raw_input("day ")

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print month_name + ' ' + ordinal + ',' + year