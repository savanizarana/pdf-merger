import PyPDF2 as pd

pdffiles = ["1.pdf","2.pdf"]
merger = pd.PdfMerger()
for filename in pdffiles:
    pdfFile = open(filename,'rb')
    pdfReader = pd.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
