import PyPDF2 as pdf

pdffile = open("fileStudy.pdf",'r',encoding= "Indentity-H")
pdfreader = pdf.PdfFileReader(pdffile,)
print(pdfreader.numPages)
page = pdfreader.getPage(0)
print(page.extractText())