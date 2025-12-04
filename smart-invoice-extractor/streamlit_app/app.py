import streamlit as st
from src.pdf_reader import extract_text_from_pdf
from src.ocr_extractor import ocr_from_scanned_pdf
from src.data_parser import parse_invoice_text
from src.save_results import save_to_excel

st.title("📄 Smart Invoice Data Extractor")

uploaded_file = st.file_uploader("Upload Invoice PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("temp.pdf")

    if len(text.strip()) < 20:
        st.info("Using OCR for scanned PDF...")
        text = ocr_from_scanned_pdf("temp.pdf")

    df = parse_invoice_text(text)
    save_to_excel(df)

    st.success("Extraction Complete! Download below:")
    st.dataframe(df)

    with open("output/extracted_data.xlsx", "rb") as file:
        st.download_button("Download Excel", file, file_name="invoice_data.xlsx")
