'''Give total time experienced for your program'''
from datetime import datetime, timedelta

start_time = datetime.now()
print 'Program start.'
# your code here
for i in range(10000):
    i = i+2
    for j in range(i):
        j = j + 1

delta = datetime.now() - start_time
# remove microseconds by making it to 0
delta -= timedelta(microseconds=delta.microseconds)

print 'Program experienced', delta, 'to complete.'
