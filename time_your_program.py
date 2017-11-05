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


'''Following codes are from Intro to Algorithms (Udacity) forum @rupdawg'''
import matplotlib.pyplot as plt
import time

print 'Timer'
def Timer(num_tests, fn, *args):
    "Call function with args, num_tests times; return the average time in seconds and result."
    t0 = time.clock()
    for i in range(num_tests):
        result = fn(*args)
    t1 = time.clock()
    return (t1-t0)/num_tests, result

def plot(x, y, xy_label, output_file):
    "plot results"
    plt.figure()
    plt.hold(True)
    plt.plot(x, y, label=xy_label)
    plt.legend(loc=4)
    plt.savefig(output_file)
    #plt.show()

def naive(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def rec_naive(a, b):
    if a == 0:
        return 0
    return b + rec_naive(a-1, b)

def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

def rec_russian(a, b):
    if a == 0: return 0
    if a%2 == 0: return rec_russian(a/2, b)
    return b + rec_russian((a-1)/2, b)

maxsize = 24
ns  = [1 << i for i in range(maxsize)]
ns2 = [1.0*ns[i]/ns[-1] for i in range(maxsize)]

timesn = [Timer(1, naive, n, n)[0] for n in ns]
plot(ns2, timesn, 'Time (sec) for naive(n,n)  versus  n/(2**'   + str(maxsize-1) + ')', 'naive.png')

timesn = [Timer(1, rec_naive, n, n)[0] for n in range(24)]
plot(ns2, timesn, 'Time (sec) for naive(n,n)  versus  n/(2**'   + str(maxsize-1) + ')', 'rec_naive.png')

timesr = [Timer(100000, russian, n, n)[0] for n in ns]
plot(ns2, timesr, 'Time (sec) for russian(n,n)  versus  n/(2**' + str(maxsize-1) + ')', 'russian.png')

timesr = [Timer(100000, rec_russian, n, n)[0] for n in ns]
plot(ns2, timesr, 'Time (sec) for russian(n,n)  versus  n/(2**' + str(maxsize-1) + ')', 'rec_russian.png')
print 'pngs written to file.'
