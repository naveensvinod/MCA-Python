class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,obj2):
        if obj1.area()>obj2.area():
            print("greater area=",obj1.area)
        else:
            print("greater area=",obj2.area())
length=int(input("enter the length of rectangle1 ="))
breadth=int(input("enter the breadth of rectangle1 ="))
obj1=rectangle(length,breadth)
print("Area of rectangle1=",obj1.area())
print("perimeter of rectangle1=",obj1.perimeter())
print()
length1=int(input("enter the length of rectangle2 ="))
breadth1=int(input("enter the breadth of rectangle2 ="))
obj2=rectangle(length1,breadth1)
print("Area of rectangle2=",obj2.area())
print("perimeter of rectangle2=",obj2.perimeter())
obj1.compare(obj2)