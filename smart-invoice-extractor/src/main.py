from src.pdf_reader import extract_text_from_pdf
from src.ocr_extractor import ocr_from_scanned_pdf
from src.data_parser import parse_invoice_text
from src.save_results import save_to_excel

def run_extraction(pdf_path):
    print("Extracting text from PDF...")

    text = extract_text_from_pdf(pdf_path)

    if len(text.strip()) < 20:
        print("Low text detected — using OCR...")
        text = ocr_from_scanned_pdf(pdf_path)

    df = parse_invoice_text(text)
    save_to_excel(df)

    print("Extraction complete! Saved to output/extracted_data.xlsx")

if __name__ == "__main__":
    run_extraction("examples/sample_invoice.pdf")
