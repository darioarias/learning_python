from PyPDF2 import PdfFileWriter 

pdf_writer = PdfFileWriter()

pdf_writer.addBlankPage(width=72*8, height=72*11)

with open("blank.pdf", mode="wb") as file:
  pdf_writer.write(file)