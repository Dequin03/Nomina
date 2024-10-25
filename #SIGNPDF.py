#SIGNPDF
from PyPDF2 import PdfReader, PdfWriter
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Generar claves RSA (privada y pública)
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Función para firmar los datos con la clave privada
def sign_data(data, private_key):
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Función para agregar una página de firma visual y firmar electrónicamente el PDF
def sign_pdf(input_pdf_path, output_pdf_path, private_key, signer_name="ENCARGADO"):
    # Leer el PDF de entrada
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Crear un archivo temporal para la firma visual en una página en blanco
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    c.drawString(100, 50, f"Firmado electrónicamente por: {signer_name}")
    c.save()

    # Mover al inicio del archivo de la firma
    packet.seek(0)

    # Leer la firma visual como una nueva página
    new_pdf = PdfReader(packet)
    signature_page = new_pdf.pages[0]

    # Agregar todas las páginas del PDF original
    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])

    # Agregar la página de la firma visual al final
    writer.add_page(signature_page)

    # Leer el contenido original del PDF para firmar
    with open(input_pdf_path, 'rb') as f:
        pdf_data = f.read()

    # Crear la firma digital usando la clave privada
    signature = sign_data(pdf_data, private_key)

    # Agregar los metadatos de la firma
    writer.add_metadata({
        '/Signature': signature.hex(),
        '/Signer': signer_name
    })

    # Escribir el nuevo PDF firmado
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)

# Uso del código
private_key, public_key = generate_keys()

# Guardar las claves en formato PEM si es necesario
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Puedes guardar las claves en archivos si lo deseas
with open("private_key.pem", "wb") as f:
    f.write(private_key_pem)

with open("public_key.pem", "wb") as f:
    f.write(public_key_pem)

# Rutas del PDF de entrada y de salida
input_pdf = "C:\\Users\\usuario\\Downloads\\Nomina\\output\\Reporte_Semana_del_14-10-2024_al_20-10-2024.pdf"
output_pdf = "C:\\Users\\usuario\\Downloads\\Nomina\\output\\Reporte_Semana_del_14-10-2024_al_20-10-2024_firmado.pdf"

# Firmar el PDF
sign_pdf(input_pdf, output_pdf, private_key, signer_name="ENCARGADO")

print("PDF firmado con éxito.")