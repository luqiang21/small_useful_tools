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

# import pdb
#
# def f1(some_arg):
#     print some_arg
#     some_other_arg = some_arg + 1
#     return f2(some_other_arg)
#
# def f2(some_arg):
#     print some_arg
#     some_other_arg = some_arg + 1
#     return f3(some_other_arg)
#
# def f3(some_arg):
#     print some_arg
#     some_other_arg = some_arg + 1
#     return f4(some_other_arg)
#
# def f4(some_arg):
#     print some_arg
#     some_other_arg = some_arg + 1
#     return some_other_arg
#
# if __name__ == "__main__":
#     pdb.runcall(f1, 1)



#!/usr/bin/env python

import pdb
import string
import sys

class ConvertToDict:
    def __init__(self):
        self.tmp_dict = {}
        self.return_dict = {}
    def walk_string(self, some_string):
        '''walk given text string and return a dictionary.
        Maintain state in instance attributes in case we hit an exception'''
        l = string.split(some_string)
        for i in range(len(l)):
            key = str(i)
            self.tmp_dict[key] = int(l[i])
        return_dict = self.tmp_dict
        self.return_dict = self.tmp_dict
        self.reset()
        return return_dict
    def reset(self):
        '''clean up'''
        self.tmp_dict = {}
        self.return_dict = {}
    def get_number_dict(self, some_string):
        '''do super duper exception handling here'''
        try:
            return self.walk_string(some_string)
        except:
            #modified exception handler - drop us into a debugger
            tb = sys.exc_info()[2]
            pdb.post_mortem(tb)
            #if we hit an exception, we can rely on tmp_dict
			# being a backup to the point of the exception
            return self.tmp_dict

def main():
    ctd = ConvertToDict()
    for line in file(sys.argv[1]):
        line = line.strip()
        print "*" * 40
        print "line>>", line
        print ctd.get_number_dict(line)
        print "*" * 40

if __name__ == "__main__":
    main()
