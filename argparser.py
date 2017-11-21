import argparse


parser = argparse.ArgumentParser()
parser.add_argument('required', help='required field')
# optional argument start with - (abbreviation) or -- (full name)
parser.add_argument('-o', '--option',dest='optional_list',type=int, action='append', help='optional arguments')
parser.add_argument('-t', '--true', dest='default_false', action='store_true', help='this variable is False defaultly, if selected, it becomes True')
args = parser.parse_args()
required = args.required
optional_list = args.optional_list
default_false = args.default_false

print('arguments are:')
print('required:', required)
print('optional_list:', optional_list)
print('default_false:', default_false)

# help: python argparser.py -h
# usage: python argparser.py me -o 13 -o 12 -t
