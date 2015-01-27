print '''""""""""""\
""""""""'''
print '------------------------'
print 'what \'s' 'you name'
print '------------------------'
# can not use chinese
#var numi
i = 5 ;print i+1
# add ; to chat the code
i=5
print 'value is'
print '------------------------'
print True==0,True==1;
# True Flase
print '------------------------'
print 0 and 1
# and = &
print '------------------------'
print 0 or 1
# or = |
print '------------------------'
print not 2
# not x
print '------------------------'
print 'i' in 'int'
# in 
print '------------------------'
print 'i' not in 'int'
# not in
print '------------------------'
print 0|1
print '------------------------'
print 0>1
print -5
leth=5
br = 2;
print leth*br
num = 32;
# guess = int(raw_input('enter a num:'))
# raw_input means input 
# if guess == num:
# 	print "true"
# elif guess>num:
# 	print "guess > num"
# elif guess<num:
# 	print "guess < num" 

number = 30
isStop = False
while isStop:
	guess = int(raw_input("enter a num:"))
	if guess == num:
		print "is  true "
		isStop = False;
	elif guess<num:
		print "error";
	else:
		print "error lose"
else:
	print "loop is over"
# loop for while
for i in range(1,10):
	print i
else:
	print "the loop is over"

# def function 
def sayHello():
	print "sayHello is use";
sayHello();
def func():
	global x
	print x;
	x=2;
	print "changed x to",x
x = 30;
func();
print x
# use default value
def use_default(time=7):
	print time
use_default(10)