import openpyxl

excelFile=openpyxl.load_workbook("example.xlsx")

print(str(excelFile.get_sheet_names()))
