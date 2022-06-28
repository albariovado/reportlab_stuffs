from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4 # Import many different page sizes
from reportlab.platypus import SimpleDocTemplate

def print_pdf(list_of_pdf_items,document_name):
  
  # Create a pdf file and define its properties:
  pdf = SimpleDocTemplate('{}.pdf'.format(document_name),pagesize=A4,leftMargin=2*cm,rightMargin=2*cm,topMargin=2*cm,bottomMargin=2*cm)

  # Before building the pdf it is necessary to define each single element and insert it in an ordered list.
  # The order of the list will match the one shown in the pdf.
  # In this repository you'll find out files that explain how to create each element that you can insert in pdfs.
  
  # Build your pdf file:
  pdf.build(list_of_pdf_items)
