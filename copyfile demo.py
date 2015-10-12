__author__ = 'Administrator'
# coding=gbk
import shutil;
import os;
import md5

f = open("asset.txt","w")
asset = ""
for dirpath,dirnames,filenames in os.walk("E:\DTLWallPaper"):
    for filename in filenames:
        print "Ŀ¼",dirpath+"\\"+filename
        path = os.path.join(dirpath,filename);
        target = "f:/BigIcon"
        m = md5.new()
        m.update(filename);
        md = m.hexdigest()
        targetName = os.path.join(target,md)
        shutil.copyfile(path,targetName)
        asset += path +">>>>>>>>>>"+md+"\n";
f.write(asset);
f.close();
print "copy complete"