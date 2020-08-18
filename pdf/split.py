from PyPDF2 import PdfFileWriter, PdfFileReader

# 开始页
start_page = 0

# 截止页
end_page = 2

output = PdfFileWriter()
pdf_file = PdfFileReader(open("D:\data\out.pdf", "rb"))
pdf_pages_len = pdf_file.getNumPages()

# 保存input.pdf中的1-5页到output.pdf
for i in range(start_page, end_page):
 output.addPage(pdf_file.getPage(i))

outputStream = open("output.pdf", "wb")
output.write(outputStream)


def spilt_pdf(scope):
  start_page = 0
  output = PdfFileWriter()
  pdf_file = PdfFileReader(open("D:\data\out.pdf", "rb"))
  pdf_pages_len = pdf_file.getNumPages()
  for i in range(start_page, pdf_pages_len):
   for j in range(j,scope):
      output.addPage(pdf_file.getPage(j))
      outputStream = open("output.pdf", "wb")
      output.write(outputStream)