import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from utils import create_password,create_pdf
import os
from pdf_mail import sendpdf 
from dotenv import load_dotenv


load_dotenv()

# def send_email_function(email):
#     password = create_password(email)
#     pdf = create_pdf(password,email)
#     msg = MIMEMultipart()
#     msg['From'] = "sumitraghuvanshi413@gmail.com" 
#     msg['To'] = email  
#     msg['Subject'] = pdf 

    
#     body = "Please find the attached PDF document."
#     msg.attach(MIMEText(body, 'plain'))

#     # Attach the PDF file
#     try:
#         with open(pdf, "rb") as attachment:
#             part = MIMEBase('application', 'octet-stream')
#             part.set_payload(attachment.read())
#             encoders.encode_base64(part)  
#             part.add_header('Content-Disposition', f'attachment; filename={pdf.split("/")[-1]}') 
#             msg.attach(part) 
#     except Exception as e:
#         print(f"Failed to attach PDF: {e}")
#         return

#     # Send the email
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as s:
#             s.starttls()  
#             s.login("sumitraghuvanshi413@gmail.com", "aajo rgza kjpp ioat")  
#             s.send_message(msg)  
#             print(f"Email sent to {email}")
#     except Exception as e:
#         print(f"Failed to send email: {e}")
#     try:
#         os.remove(pdf)
#     except OSError as e:
#         print(f"Error deleting file {pdf}: {e}")        

def send_email_function(email):
    password = create_password(email)
    sender_email_address = os.getenv("SENDER_EMAIL_ADDRESS")
    receiver_email_address = email
    sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")
    subject_of_email = "THE NAME IS THOMAS SHALBEY"
    body_of_email = "This pdf will open with the password"
    filename = create_pdf(password,email)
    print(filename,"--------------------------")
    location_of_file = os.getcwd()
    print(location_of_file)
    k = sendpdf(
        sender_email_address,  
        receiver_email_address, 
        sender_email_password, 
        subject_of_email, 
        body_of_email, 
        filename, 
        location_of_file
    )
    k.email_send()
    try:
        os.remove(filename+".pdf")
    except OSError as e:
        print(f"Error deleting file {filename}: {e}")
