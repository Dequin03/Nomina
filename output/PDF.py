from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pikepdf

def encrypt_pdf(input_pdf, output_pdf, user_password, owner_password):
    # Encrypt the PDF using pikepdf
    with pikepdf.open(input_pdf) as pdf:
        pdf.save(
            output_pdf,
            encryption=pikepdf.Encryption(
                user=user_password,
                owner=owner_password,
                allow=pikepdf.Permissions(extract=False, print_lowres=False, modify_annotation=False,modify_assembly=False,modify_form=False,modify_other=False)
            )
        )

# Set file paths and passwords
original_pdf = r"C:\Users\usuario\Downloads\Nomina\output\output.pdf"
encrypted_pdf = "protected_document.pdf"
user_password = "userpass123"
owner_password = "ownerpass456"

# Create the PDF and then encrypt it
encrypt_pdf(original_pdf, encrypted_pdf, user_password, owner_password)

print("Encrypted PDF created successfully.")