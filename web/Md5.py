__author__ = 'Administrator'
import md5
import _md5
import hashlib
# from hashlib import md5
import math
src = "shenliangliang"
m1 = md5.new()
m1.update(src)
print m1.hexdigest()
print m1.hexdigest()
print m1.hexdigest()
print m1.hexdigest()

print "===================other use================="
m2 = _md5.new()
m2.update("shenliangliang")
m2.update("926326")
print m2.hexdigest()
print "====================================="
m3 = hashlib.md5()
m3.update(src)
m3.update("926326")
# m3.digest()
print m3.hexdigest()
