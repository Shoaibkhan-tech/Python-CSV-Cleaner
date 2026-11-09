import pandas as pd

# Step 1: Read the original CSV file
df = pd.read_csv("input.csv")

print("Original data:")
print(df)

# Step 2: Remove completely empty rows
df = df.dropna(how="all")

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Remove extra spaces from text
for column in df.select_dtypes(include=["object", "str"]).columns:
    df[column] = df[column].str.strip()

# Step 5: Save cleaned data
df.to_csv("cleaned_output.csv", index=False)

print("\nCSV cleaning completed successfully!")
print("Rows remaining:", len(df))