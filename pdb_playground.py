# '''play with python debugger here'''
# import pdb
# a = 'aaa'
# pdb.set_trace()
# b = 'bbb'
# c = 'ccc'
# final = a + b + c
# print final
#
# '''debug with subroutine'''
# def combine(s1, s2): # define subroutine combine
#     s3 = s1 + s2 + s1 # sandwiches s2 between copies of ...
#     s3 = '"' + s3 + '"' # encloses it in double quotes
#     return s3
#
# a = 'aaa'
# import pdb
# pdb.set_trace()
# b = 'bbb'
# c = 'ccc'
# final = combine(a, b)
# print final

#!/usr/bin/env python

import pdb

def f1(some_arg):
    print some_arg
    some_other_arg = some_arg + 1
    return f2(some_other_arg)

def f2(some_arg):
    print some_arg
    some_other_arg = some_arg + 1
    return f3(some_other_arg)

def f3(some_arg):
    print some_arg
    some_other_arg = some_arg + 1
    return f4(some_other_arg)

def f4(some_arg):
    print some_arg
    some_other_arg = some_arg + 1
    return some_other_arg

if __name__ == "__main__":
    pdb.runcall(f1, 1)
