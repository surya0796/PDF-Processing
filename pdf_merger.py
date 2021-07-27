import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger =  PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    with open('merged_pdf.pdf','wb') as file:
        merger.write(file)    
            
pdf_combiner(inputs)
        

        
        
