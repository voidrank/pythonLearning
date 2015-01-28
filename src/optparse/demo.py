from optparse import OptionParser
import sys


parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
options, argv = parser.parse_args(sys.argv[1:])
print(options)
print(argv)
