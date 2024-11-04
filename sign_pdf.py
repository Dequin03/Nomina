#Firma PDF
# Import Libraries
from datetime import datetime, timedelta
import OpenSSL
import os
import fitz  # PyMuPDF
import time
import argparse
from PDFNetPython3.PDFNetPython import *
from cryptography.hazmat.primitives import serialization
from cryptography import x509

from cryptography.x509.oid import NameOID

from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives.asymmetric import padding  
from typing import Tuple


def createKeyPair():
    """
    Create a public/private key pair
    Arguments: Type - Key Type, must be one of TYPE_RSA and TYPE_DSA
               bits - Number of bits to use in the key (1024 or 2048 or 4096)
    Returns: The public/private key pair in a PKey object
    """
    pkey = rsa.generate_private_key(

    public_exponent=65537,

    key_size=2048,

)
    return pkey
def create_self_signed_cert(key):
    """Create a self-signed certificate."""
    # Create a self-signed certificate
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, "mysite.com"),
    ])
    
    # Build the certificate
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(subject)  # Self-signed, so subject and issuer are the same
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))  # Valid for 1 year
        .add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )
        .sign(key, hashes.SHA256())
    )
    
    return cert

def load():
    """Generate the certificate"""
    summary = {}
    summary['OpenSSL Version'] = OpenSSL.__version__
    
    # Generating a Private Key...
    key = createKeyPair()
    
    # PEM encoded
    with open('C:\\Users\\usuario\\Downloads\\static\\private_key.pem', 'wb') as pk:
        pk.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))

    # Generating a self-signed client certificate...
    cert = create_self_signed_cert(key)
    with open('C:\\Users\\usuario\\Downloads\\static\\certificate.cer', 'wb') as cer:
        cer.write(cert.public_bytes(serialization.Encoding.PEM))

    # Generating a PKCS12 file with the private key and the certificate...
    p12 = pkcs12.serialize_key_and_certificates(
        name=b'mysite.com',
        key=key,
        cert=cert,
        cas=None,
        encryption_algorithm=serialization.NoEncryption(),
    )

    with open('C:\\Users\\usuario\\Downloads\\static\\container.pfx', 'wb') as pfx:
        pfx.write(p12)

    # Display Summary
    print("## Initialization Summary ##################################################")
    print("\n".join("{}: {}".format(i, j) for i, j in summary.items()))
    print("############################################################################")
    return True
def sign_file(input_file: str, signatureID: str, x_coordinate: int, 
              y_coordinate: int, pages: Tuple = None, output_file: str = None):
    """Sign a PDF file using PyMuPDF and add a visible signature"""
    
    if not output_file:
        output_file = os.path.splitext(input_file)[0] + "_signed.pdf"
    
    # Load the PFX certificate
    with open('C:\\Users\\usuario\\Downloads\\static\\container.pfx', 'rb') as f:
        pfx_data = f.read()
    
    private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
        pfx_data, None
    )
    
    # Open the PDF document
    pdf_document = fitz.open(input_file)
    
    # Iterate through the pages
    for page_num in range(pdf_document.page_count):
        if pages and page_num + 1 not in pages:
            continue
        
        page = pdf_document.load_page(page_num)
        
        # Define the position of the signature
        rect = fitz.Rect(x_coordinate, y_coordinate, x_coordinate + 100, y_coordinate + 50)
        
        # Add the signature image (optional, you can modify this path to your actual image)
        sign_image = os.path.join(os.path.dirname(__file__), "static", "signature.png")
        page.insert_image(rect, filename=sign_image)
    
    # Save the PDF with the visible signature
    pdf_document.save(output_file)
    
    # Now we proceed to create the hash and sign the document using the private key
    with open(output_file, 'rb') as f:
        pdf_data = f.read()
    
    # Hash the PDF data
    digest = hashes.Hash(hashes.SHA256())
    digest.update(pdf_data)
    pdf_hash = digest.finalize()
    
    # Sign the hash with the private key
    signature = private_key.sign(
        pdf_hash,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    
    # Append the signature as metadata or store it in a field (this example just prints it)
    print(f"Digital signature: {signature.hex()}")
    
    # You can choose to embed the signature in the PDF metadata or in a dedicated field.
    
    print(f"PDF signed and saved to {output_file}")
    return True

def is_valid_path(path):
    if not path:
        raise ValueError(f"invalid Path")
    if os.path.isfile(path):
        return path
    elif os.path.isdir(path):
        return path
    else:
        raise ValueError(f"Invalid Path")

def parse_args():
    parser=argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-l','--load',dest='load', action="store_true",
                        help="Load the required configurations and create the certificate")
    parser.add_argument('-i','--input_path',dest='input_path', type=is_valid_path,
                        help="Enter the path of the file or the folder to process")
    parser.add_argument('-s','--signatureID', dest='signatureID',
                        type=str, help="Enter the ID of the signature")
    parser.add_argument('-p','--pages', dest='pages', type=tuple,
                        help="Enter the pages to consider e.g.: [1,3]")
    parser.add_argument('-x','--x_coordinate', dest='x_coordinate',
                        type=int, help="Enter the x coordinate.")
    parser.add_argument('-y','--y_coordinate', dest='y_coordinate',
                        type=int, help="Enter the y coordinate.")
    path=parser.parse_known_args()[0].input_path
    if path and os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file',
                            type=str, help="Enter a valid output file")
    if path and os.path.isdir(path):
        parser.add_argument('-r', '--recursive', dest='recursive', default=False, type=lambda x: (
            str(x).lower() in ['true', '1', 'yes']), help="Process Recursively or Non-Recursively")
    args = vars(parser.parse_args())
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args

if __name__=="__main__":
    args=parse_args()
    if args['load']==True:
        load()
    else:
        if os.path.isfile(args['input_path']):
            sign_file(
                input_file=args['input_path'],signatureID=args['signatureID'],
                x_coordinate=int(args['x_coordinate']), y_coordinate=int(args['y_coordinate']),
                pages=args['pages'],output_file=args['output_file']
            )
        elif os.path.isdir(args['input_path']):
            print("a")