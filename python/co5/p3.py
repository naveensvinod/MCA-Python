import csv
f1=open("studentdetails.csv",'r')
reader=csv.reader(f1)
for line in reader:
    print(line[2])
    