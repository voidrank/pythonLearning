from optparse import OptionParser
import sys


parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="specify the filename to generatr", metavar="FILE")

options, args = parser.parse_args(sys.argv[1:])
filename = options.filename
f = open(filename, "wb")
f.close()
