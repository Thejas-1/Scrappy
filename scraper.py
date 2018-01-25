#import pdfquery
#pdf = pdfquery.PDFQuery("sample.pdf")
#pdf.load()
#label = pdf.pq(':contains("Your first name and initial")')
#left_corner = float(label.attr('x0'))
#bottom_corner = float(label.attr('y0'))
#name = pdf.pq(':in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner-30, left_corner+150, bottom_corner)).text()
#print name
import re
import PyPDF2
newfile = open('hello.txt','w')
file=open('sample.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
pageobj=pdfreader.getPage(10)
newfile.write(pageobj.extractText())
file.close()
newfile.close()

with open('hello.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
#print data
#print len(data)
print '\n'
print (re.split((']'),data))
w = (re.split((']'),data))

n = len(w)
m = n-2
k = w[m]
print k 
o = (re.split(('\['),k))
print o[1]
#s = len(k)
#e = k[s-1]
#print e
#len1 = len(k)
#n1 = k-
#i1 = int(re.search(r'\d+',k).group())
#i2 = map(int, re.findall(r'\d+', k))
#print i1
#print i2
#s = ''.join(x for x in k if x.isdigit())
#print int(s)
myfile.close()
