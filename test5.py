# multiprocessing.py
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
    #while True:
    #	a = 3*2
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
    #while True:
    #	b = 4*5