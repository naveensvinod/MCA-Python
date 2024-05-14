l1=[1,3,4,5,7]
l2=[2,3,4,6,8,9]
if len(l1)==len(l2):
    print('equal length')
else:
    print('not equal length')
if sum(l1)==sum(l2):
    print('The sums are equal =',c)
else:
    print('the sums are not equal')
l3=[elem for elem in l1 if elem in l2]
if len(l3)>0:
    print('the common elements are ',l3)
else:
    print('there are no common elements')
    