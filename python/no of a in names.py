names=['naveen ','Amal','Anas','gopan','aliyan']
count=0
for names in names:
    count=count+names.count('a')+names.count('A')
print('the occurance of a in list is :',count)