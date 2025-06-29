# Test Cases :
# Template renders expected values.
# PDF is generated and not empty.
# Test cleanup removes temp files.

# How to Run unit test
# cmd : python -m unittest fileName

import unittest
import os
from jinja2 import Environment, FileSystemLoader
import pdfkit

class TestInvoiceGenerator(unittest.TestCase): #TestCase is a class inherited from unittest i.e a built-in module of python

    def setUp(self):
        # Setup template environment
        self.loader = FileSystemLoader('.')
        self.env = Environment(loader=self.loader)
        self.contents = {
            'client_name': "Test Client",
            'item1': 'Item A',
            'item2': 'Item B',
            'item3': 'Item C',
            'subtotal1': 100,
            'subtotal2': 200,
            'subtotal3': 300,
            'today_date': '01 Jan, 2025',
            'month': 'January',
            'total': 600
        }
        self.template_name = 'invoice.html'
        self.output_pdf = 'test_output.pdf'
        self.wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

    def test_template_renders(self):
        # Load and render template
        template = self.env.get_template(self.template_name)
        rendered = template.render(self.contents)
        # Check if some expected text exists in rendered template
        self.assertIn(self.contents['client_name'], rendered)
        self.assertIn(str(self.contents['total']), rendered)

    def test_pdf_generation(self):
        template = self.env.get_template(self.template_name)
        output_text = template.render(self.contents)

        config = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)
        # Generate PDF
        pdfkit.from_string(output_text, self.output_pdf, configuration=config)

        # Check if PDF file is created and has some size
        self.assertTrue(os.path.exists(self.output_pdf))
        self.assertGreater(os.path.getsize(self.output_pdf), 0)

    def tearDown(self):
        # Clean up created PDF after tests
        if os.path.exists(self.output_pdf):
            os.remove(self.output_pdf)

if __name__ == '__main__':
    unittest.main()
