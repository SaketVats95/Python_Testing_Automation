import csv

write_file=open("write.csv",'w',newline='')
writer=csv.writer(write_file)
writer.writerow(['Animal Names:','Cat','Dog','Cow','Buffalow','Goat','Chicken'])
writer.writerow(['Fruits Names:','Guava','Graves','Banana','Orange'])

write_file.close()
