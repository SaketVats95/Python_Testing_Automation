import csv,os

os.makedirs("headerRemoved",exist_ok=True)
path='D:\\Python\\Travel\\CSV Testing\\excelSpreadsheets\\'
for csvFiles in os.listdir('D:\\Python\\Travel\\CSV Testing\\excelSpreadsheets'):
    if not csvFiles.endswith('.csv'):
        continue

    else:
        print("Files name from where we have to remove header ",csvFiles)
        csvRows=[]
        csvFile=open(path+csvFiles)
        readerObj=csv.reader(csvFile)
        for i in readerObj:
            if readerObj.line_num==1:
                continue
            else:
                csvRows.append(i)
        csvFile.close()

        csvFileWrite=open(os.path.join("headerRemoved",csvFiles),'w',newline='')
        csvWriter=csv.writer(csvFileWrite)
        for i in csvRows:
            csvFileWrite.write(str(i))
        csvFileWrite.close()
