from optparse import OptionParser
import sys


parser = OptionParser()
parser.add_option("-y", action="store_true", dest="verbose")
parser.add_option("-n", action="store_false", dest="verbose")

parser.add_option("--store-const", action="store_const", dest="a_const")
parser.add_option("--append-to-list", action="append", dest="a_list")
parser.add_option("--count", action="count", dest="count")

print(parser.parse_args(sys.argv[1:]))
