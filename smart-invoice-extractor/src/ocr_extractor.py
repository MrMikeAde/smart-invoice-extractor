import pytesseract
from PIL import Image
import pdfplumber

def ocr_from_scanned_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            img = page.to_image(resolution=300).original
            text += pytesseract.image_to_string(Image.fromarray(img))
    return text.strip()
