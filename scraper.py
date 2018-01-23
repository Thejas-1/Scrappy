#import pdfquery
#pdf = pdfquery.PDFQuery("sample.pdf")
#pdf.load()
#label = pdf.pq(':contains("Your first name and initial")')
#left_corner = float(label.attr('x0'))
#bottom_corner = float(label.attr('y0'))
#name = pdf.pq(':in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()
#print name

import PyPDF2
newfile = open('hello.txt','w')
file=open('sample.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
pageobj=pdfreader.getPage(103)
newfile.write(pageobj.extractText())
file.close()
newfile.close()
