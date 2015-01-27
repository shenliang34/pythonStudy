import os
import time
soure =[r'C:\back',r'C:\back']
target_dir=r'C:\backup'
target = target_dir+time.strftime('%Y%M%d%H%M%S')+'.zip'
zip_comman="zip -qr '%s' %s" % (target, ' '.join(soure))
if os.system(zip_comman) == 0:
	print "Successful to backup",target
else:
	print 'Failed to backup'