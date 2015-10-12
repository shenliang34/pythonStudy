__author__ = 'Administrator'
try:
    i=9
    j="sf"
    print i+j
except NameError:
    print "error"
except TypeError:
    print "type error"
try:
    for i in range(0,10):
        print i
        if i == 7:
            raise NameError
except NameError:
    print "error"

class MyError(Exception):
    def __init__(self):
        print("My error")
        Exception.__init__(self)
try:
    for i in range(0,10):
        print i
        if i == 7:
            raise MyError
except MyError,e:
    print "my error"
finally:
    print "finally"