import win32com.client as win32
import os

def excel_to_pdf(excel_file, pdf_file):
    # Initialize Excel application (headless)
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False  # Keep Excel hidden

    # Open the workbook
    workbook = excel.Workbooks.Open(excel_file)

    # Save as PDF
    workbook.ExportAsFixedFormat(0, pdf_file)

    # Close the workbook and Excel application
    workbook.Close(SaveChanges=False)
    excel.Quit()

    # Clean up resources
    del excel

# Specify the Excel and PDF file paths
excel_file = os.path.abspath("C:\\Users\\usuario\\Downloads\\Nomina\\Formatollenado.xlsx")
pdf_file = os.path.abspath("C:\\Users\\usuario\\Downloads\\Nomina\\output\\output.pdf")

# Run the conversion
excel_to_pdf(excel_file, pdf_file)

print("Excel file has been successfully saved as a PDF.")