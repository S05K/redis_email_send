from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import os
import re

def create_pdf(user_password, user_email):
    # Create a simple PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello, Welcome!", ln=True, align='C')
    
    # Save the PDF to file
    file_path = f"{user_email}_welcome.pdf"
    pdf.output(file_path)
    
    # Apply password protection
    with open(file_path, "rb") as original_pdf:
        reader = PdfReader(original_pdf)
        writer = PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)
        
        # Add user password
        writer.encrypt(user_password)
        
        protected_pdf_path = f"{user_email}_welcome.pdf"
        with open(protected_pdf_path, "wb") as protected_pdf:
            writer.write(protected_pdf)
    
    protected_pdf_path = protected_pdf_path[:-4]
    return protected_pdf_path




def create_password(email):
    l=len(email)-4
    new_str=str()
    for i in range(l):
        new_str=new_str+(email[i])
    lst=list(new_str)
    print(new_str)
    password_list=str()
    for i in lst:
        if i=='@':
            var=lst.index(i)
            for j in range((var-2),var+3):
                password_list=password_list+lst[j]
    print(password_list)
    return password_list
    