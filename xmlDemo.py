# encoding:utf-8

# xmlFile = open("language.xml","r")
#
# line = xmlFile.readline()
# epp.1
# while line:
#     print line
#     line = xmlFile.readline()

# epp.2
# for line in open("language.xml"):
#     print line

# file = open("language.xml","r")
# lines = file.readlines()
#
# str = ""
# for line in lines:
#     str += line
#     # print line
# print str.strip().split("")

import xml.dom.minidom

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  

languageAs = "Language.as"
xmlPath = "language.xml"

file = open(languageAs,"w")

dom = xml.dom.minidom.parse(xmlPath)

root = dom.documentElement

start = "package com.gamehero.sxd2.pro\n{"
file.write(start + "\n")
file.write("\tpublic class Language\n\t{" + "\n")

languages = root.getElementsByTagName("language")

dic = {}

def parsexml():
    for language in languages:
        key =  language.getAttribute("key")
        value = language.getAttribute("value")
        if(dic.has_key(key) == False):
    		file.write("\t\tpublic static const " + key + ":String = " +"\""+ value.decode('utf-8').strip("\r") +"\""+ ";" + "\n")
    		dic[key] = value.decode('utf-8')
    	else:
    		print dic[key]
    file.write("\t}\n")
    file.write("}")
    file.close()
    # print dic
    print "end"
        # file.write(key + value)

package = "package com.gamehero.sxd2.pro\n { \n public class Language{"
parsexml()

