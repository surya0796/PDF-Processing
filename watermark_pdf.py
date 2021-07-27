import PyPDF2
import sys

inputs = sys.argv[:]

def watermark_adder(input_pdf,output_pdf ,watermark_pdf):
    watermark_read = PyPDF2.PdfFileReader(watermark_pdf)
    watermark_page = watermark_read.getPage(0)
    input_read = PyPDF2.PdfFileReader(input_pdf)
    writer = PyPDF2.PdfFileWriter()

    for page in range(input_read.getNumPages()):
        page = input_read.getPage(page)
        page.mergePage(watermark_page)
        writer.addPage(page)
    with open(output_pdf,'wb') as file:
        writer.write(file)
watermark_adder(inputs[1],inputs[2],inputs[3])        

