# Project Name : Invoice Generator (GUI + PDF)
# Create a Python app that generates professional invoices and exports them to PDF.
# Author : Roman Zapatmar
# Date : 06 June 2025
# Description : Create Invoice PDF using python. I will use fpdf library
# a project with custom template and css and also with invoice template to generate pdf
# source link : https://www.youtube.com/watch?v=1IYtkkEOuoU    
# libraries : jinja2(pip install jinja2), pdfkit -(pip install pdfkit)
# unitTest file : test_invoice_generator.py


import jinja2
import pdfkit
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# my_name = "Roman Zapatmar"
# item1 = "Laptop"
# item2 = "Mouse"
# item3 = "Keyboard"
# today_date = datetime.today().strftime("%d %b, %Y")
# issued_by = "Roman Zapatmar"

#create a dictionary
# context = {
#     'my_name' : my_name,
#     'item1' : item1,
#     'item2' : item2,
#     'item3' : item3,
#     'today_date' : today_date,
#     'issued_by' : issued_by
# }

#invoice contents --template used here
client_name = "Andrew Smith"
item1 = 'Washing Machine'
item2 = 'Air Conditioner'
item3 = 'Refrigerator'
subtotal1 = 500
subtotal2 = 100
subtotal3 = 200
today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")
total = 1000
contents = {
    'client_name' : client_name,
    'item1' : item1,
    'item2' : item2,
    'item3' : item3,
    'subtotal1' : subtotal1,
    'subtotal2' : subtotal2,
    'subtotal3' : subtotal3,
    'today_date' : today_date,
    'month' : month,
    'total' : total
}

# Set up Jinja2 environment
loader = FileSystemLoader('.')  # bcause template is in the same folder
env = Environment(loader=loader)

# Load and render the template
template = env.get_template("invoice.html")  # NOT get_source!
output_text = template.render(contents)

#exporting pdf 
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
# pdfkit.from_string(output_text, "invoices/generated_invoice.pdf", configuration=config, css="template.css") #it will save a pdf file under the invoices folder
pdfkit.from_string(output_text, "invoices/customInvoices/custom_invoice.pdf", configuration=config, css="invoice.css") #it will save a pdf file under the invoices folder
