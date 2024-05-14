f=open('newfile1.txt','r')
lines=f.readlines()
l1=[line.strip() for line in lines]
print(l1)