import os
import cv2
import pytesseract
import re
from tabulate import tabulate

# Path to the directory containing the images
directory = r'C:\Users\xiaom\OneDrive\Desktop\CIM\Assignment\Receipt&Invoice'

# Initialize Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Keywords to identify receipts and invoices
receipt_keywords = ['receipt', 'amount', 'date']
invoice_keywords = ['invoice', 'amount', 'date']

# Regular expressions for matching the desired information
amount_regex = r'Total Amount\s+([$€£¥]\s*\d+(?:,\d+)*(?:\.\d+)?)'
receipt_no_regex = r'RECEIPT NO\.\s+(\S+)'
invoice_no_regex = r'INVOICE NO\.\s+(\S+)'
date_regex = r'(\d{1,2}/\d{1,2}/\d{4})'

# Lists to store the extracted information
receipts = []
invoices = []

# Process each image in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(directory, filename)
        image = cv2.imread(image_path)
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Perform OCR
        text = pytesseract.image_to_string(gray)
        
        # Check if the image contains a receipt
        if any(keyword in text.lower() for keyword in receipt_keywords):
            # Extract total amount
            match_amount = re.search(amount_regex, text)
            total_amount = match_amount.group(1) if match_amount else 'N/A'
            
            # Extract receipt number
            match_receipt_no = re.search(receipt_no_regex, text)
            receipt_no = match_receipt_no.group(1) if match_receipt_no else 'N/A'
            
            # Extract date
            match_date = re.search(date_regex, text)
            date = match_date.group(1) if match_date else 'N/A'
            
            receipts.append({
                'Filename': filename,
                'Receipt No.': receipt_no,
                'Date': date,
                'Total Amount': total_amount
            })
        
        # Check if the image contains an invoice
        if any(keyword in text.lower() for keyword in invoice_keywords):
            # Extract total amount
            match_amount = re.search(amount_regex, text)
            total_amount = match_amount.group(1) if match_amount else 'N/A'
            
            # Extract invoice number
            match_invoice_no = re.search(invoice_no_regex, text)
            invoice_no = match_invoice_no.group(1) if match_invoice_no else 'N/A'
            
            # Extract date
            match_date = re.search(date_regex, text)
            date = match_date.group(1) if match_date else 'N/A'
            
            invoices.append({
                'Filename': filename,
                'Invoice No.': invoice_no,
                'Date': date,
                'Total Amount': total_amount
            })

# Filter out invalid entries for receipts and invoices
valid_receipts = [receipt for receipt in receipts if receipt['Receipt No.'] != 'N/A']
valid_invoices = [invoice for invoice in invoices if invoice['Invoice No.'] != 'N/A']

# Display the results
if valid_receipts:
    print('Receipts:')
    print(tabulate(valid_receipts, headers='keys'))

if valid_invoices:
    print('\nInvoices:')
    print(tabulate(valid_invoices, headers='keys'))
