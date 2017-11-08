# '''play with python debugger here'''
# import pdb
# a = 'aaa'
# pdb.set_trace()
# b = 'bbb'
# c = 'ccc'
# final = a + b + c
# print final

'''debug with subroutine'''
def combine(s1, s2): # define subroutine combine
    s3 = s1 + s2 + s1 # sandwiches s2 between copies of ...
    s3 = '"' + s3 + '"' # encloses it in double quotes
    return s3

a = 'aaa'
import pdb
pdb.set_trace()
b = 'bbb'
c = 'ccc'
final = combine(a, b)
print final
