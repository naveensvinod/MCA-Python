l1=[]
n=int(input('enter the number of elements'))
for i in range(0,n):
    a=(input('enter the color'))
    l1.append(a)
print('colors are : ',l1,sep=',')
print("the first and last elements of the list are : ",l1[0] ,'and', l1[-1])