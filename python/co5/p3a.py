import csv
csvfile1=open("studentdetails.csv","r")
csv_reader=csv.reader(csvfile1)
for line in csv_reader:
    print(line)