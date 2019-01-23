import csv

example_file=open("example.csv")
print("Example File Type : ",type(example_file))
exampleReader=csv.reader(example_file)
print("Example Reader Type: " ,type(exampleReader))

#exampleData=list(exampleReader)
#print("Example Data Type (Explecit Conversion):", type(exampleData))

#print(exampleData)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))



