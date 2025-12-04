import pandas as pd

def save_to_excel(df, output_path="output/extracted_data.xlsx"):
    df.to_excel(output_path, index=False)

def save_to_csv(df, output_path="output/extracted_data.csv"):
    df.to_csv(output_path, index=False)
