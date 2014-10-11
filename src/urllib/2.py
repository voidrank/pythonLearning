import urllib
url = "http://caiyunapp.com/fcgi-bin/v1/api.py?lonlat=121.5069,31.2974&format=json&product=minutes_prec&token=TAkhjf8d1nlSlspN"
f = urllib.urlopen(url)
print f.read()

