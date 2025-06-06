from pdf2image import convert_from_path
import pytesseract
from pytesseract import Output
from docx import Document
from docx.shared import Pt
import os

def convert_pdf_to_docx(pdf_path, output_docx):
    # Convert each page to image
    pages = convert_from_path(pdf_path, dpi=300)
    
    # Create Word document
    doc = Document()

    for i, page in enumerate(pages):
        # OCR with layout-aware config
        text = pytesseract.image_to_string(page, config='--psm 1')  # PSM 1 = Auto layout
        doc.add_paragraph(text)
        doc.add_page_break()
    
    # Save the docx
    doc.save(output_docx)
    print(f"Saved: {output_docx}")

# Usage
convert_pdf_to_docx("Topic_Modeling_Using_LDA_and_K_Means.pdf", "output.docx")
