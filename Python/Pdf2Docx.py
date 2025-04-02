from pdf2docx import Converter
pdf_path = r"/Users/sothea/Downloads/91st_TOPIK_II_Reading.pdf"
docx_path = r"/Users/sothea/Downloads/91st_TOPIK_II_Reading.pdf.docx"
cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()