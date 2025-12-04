import re
import pandas as pd

def parse_invoice_text(text):
    data = {
        "vendor": None,
        "invoice_date": None,
        "total_amount": None
    }

    vendor_match = re.search(r"(Invoice from|Vendor|Supplier):?\s*(.*)", text)
    date_match   = re.search(r"(\d{2}[\/\.-]\d{2}[\/\.-]\d{4})", text)
    total_match  = re.search(r"(Total|Amount Due|Grand Total):?\s*([\d,]+\.\d{2})", text)

    if vendor_match:
        data["vendor"] = vendor_match.group(2).strip()
    if date_match:
        data["invoice_date"] = date_match.group(1)
    if total_match:
        data["total_amount"] = total_match.group(2)

    return pd.DataFrame([data])
