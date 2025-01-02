from spire.pdf.common import *
from spire.pdf import *

# Create an object of the PdfDocument class
doc = PdfDocument()
# Load a PDF document
doc.LoadFromFile("DOC-20241231-WA0026..pdf")

# Save the PDF document to HTML format
doc.SaveToFile("InterPrint.html", FileFormat.HTML)
doc.Close()
