import PyPDF2 as pdf

pdffiles = ["1.pdf","2.pdf"]
merger = pdf.PdfMerger()
for filename in pdffiles:
    pdfFile = open(filename,'rb')
    pdfReader = pdf.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
