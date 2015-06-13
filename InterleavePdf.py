import PyPDF2
from formlayout import fedit

paths = [('Input', ''), ('Output', '')]

pathsRead = fedit(paths, 
                  title="Interleave pdf",
                  comment="Enter the full path to the source pdf and a path to output the result."
                  )
# Full path to files should be specified eg C:\Users\Sam\Documents\Input.pdf and C:\Users\Sam\Documents\Input.pdf

document = PyPDF2.PdfFileReader(pathsRead[0])
writer = PyPDF2.PdfFileWriter()

for page in document.pages:
	writer.addPage(page)
	writer.addBlankPage()

outputStream = open(pathsRead[1], 'wb')
writer.write(outputStream)
outputStream.close()