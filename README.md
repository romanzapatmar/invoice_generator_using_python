# Python Invoice & PDF Generator

Automate the creation of professional, customizable PDF invoices using Python.

## Features
- **Clean, print-ready PDFs** – Generate neat invoices using libraries like ReportLab or PDFKit + Jinja2 templates :contentReference[oaicite:1]{index=1}.
- **Flexible templating** – Use HTML/Jinja2 to define invoice layout, easily customizable to match your branding :contentReference[oaicite:2]{index=2}.
- **Tax & total calculations** – Dynamically compute line totals, taxes (e.g., CGST/SGST/IGST), and overall invoice amount :contentReference[oaicite:3]{index=3}.
- **Logo & signature support** – Insert company logos and authorized signatures into the invoice design :contentReference[oaicite:4]{index=4}.
- **Simple and lightweight** – Requires just a few dependencies, focused on core functionality and ease of use.

## Prerequisites
- Python 3.x
- **pdfkit**, **Jinja2**, **wkhtmltopdf** (if using HTML template rendering)

## Installation
```bash
git clone https://github.com/romanzapatmar/invoice_generator_using_python.git
cd invoice-generator
pip install -r requirements.txt
# If using pdfkit:
# - Install wkhtmltopdf (e.g., `apt-get install wkhtmltopdf`, `brew install wkhtmltopdf`, or download manually)
