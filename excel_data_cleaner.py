
import pandas as pd
from google.colab import files

print("=" * 40)
print("       EXCEL DATA CLEANER")
print("=" * 40)

uploaded = files.upload()
file_name = list(uploaded.keys())[0]

df = pd.read_excel(file_name)
original_rows = len(df)

df.columns = df.columns.str.strip()
df.dropna(how="all", inplace=True)

duplicates_removed = df.duplicated().sum()
df.drop_duplicates(inplace=True)

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

cleaned_rows = len(df)
empty_rows_removed = original_rows - cleaned_rows - duplicates_removed

output_file = "cleaned_data.xlsx"
df.to_excel(output_file, index=False)

print("\n--- CLEANING REPORT ---")
print("Original rows:", original_rows)
print("Duplicates removed:", duplicates_removed)
print("Empty rows removed:", empty_rows_removed)
print("Final rows:", cleaned_rows)

print("\nCleaning completed successfully!")

files.download(output_file)
