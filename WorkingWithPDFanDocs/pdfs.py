import PyPDF2

pdffile=open('meetingminutes.pdf', 'rb')

pdfReader=PyPDF2.PdfFileReader(pdffile)

print(pdfReader.numPages)

pdfObj=pdfReader.getPage(4)

#print(pdfObj.extractText())

pdffileDec=open("encrypted.pdf",'rb')

pdfReader_e=PyPDF2.PdfFileReader(pdffileDec)
pdfReader_e.decrypt('rosebud')

print(pdfReader_e.numPages)

pdfWrite=PyPDF2.PdfFileWriter()

for i in range(pdfReader_e.numPages):
    p_page=pdfReader_e.getPage(i)
    pdfWrite.addPage(p_page)

pdf_W_file=open("new_w_file.pdf",'wb')
pdfWrite.write(pdf_W_file)
pdf_W_file.close()

