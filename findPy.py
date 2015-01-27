#encoding:utf-8
import os
for root,dirs,files in os.walk(r"."):
	print "files",files
	print "root",root
	print "dirs",dirs
	l = [os.path.splitext(pa)[0] for pa in files if os.path.splitext(pa)[1]==".py"]
	for p in l:
		print p