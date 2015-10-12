__author__ = 'Administrator'
#create file
#f = open("1.txt","w")#name,mode,
#fc = file("1.txt","w")
content = ''
f = open("1.txt","w")
for i in range(0,100):
    content += str(i)+'\n'
f.write(content)

f = file("1.txt","r")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line
f.close()