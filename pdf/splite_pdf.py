from PyPDF2 import PdfFileWriter, PdfFileReader
# def spilt_pdf(scope):
#   start_page = 0
#   output = PdfFileWriter()
#   pdf_file = PdfFileReader(open("D:\data\out.pdf", "rb"))
#   pdf_pages_len = pdf_file.getNumPages()
#
#   page=0
#   while page<pdf_pages_len:
#       for i in range(page,page+scope):
#           output.addPage(i)
#           outputStream = open("output" + str(i) + ".pdf", "wb")



# def split_pdf(scope):
#     start_page=0
#     pdf_file = PdfFileReader(open("D:\data\out.pdf", "rb"))
#     output = PdfFileWriter()
#     pdf_pages_len = pdf_file.getNumPages()
#     while start_page<=pdf_pages_len:
#
#         for i in range(start_page,scope):
#
#             output.addPage(pdf_file.getPage(i))
#         output = PdfFileWriter()
#         outputStream = open(str(i)+'.pdf','wb')
#         output.write(outputStream)
#         start_page=start_page+scope

def split_pdf():
    start_page = 0
    pdf_file = PdfFileReader(open("D:\data\out.pdf", "rb"))
    pdf_pages_len = pdf_file.getNumPages()
    for i in range(start_page,pdf_pages_len):
        output = PdfFileWriter()
        output.addPage(pdf_file.getPage(i))
        outputStream = open(str(i)+'.pdf','wb')
        output.write(outputStream)

split_pdf()
