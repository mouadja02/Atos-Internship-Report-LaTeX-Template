import pandas as pd

# Load the CSV file
df = pd.read_csv('input_data.csv')

# Display the first few rows
print("Original Data:")
print(df.head())

# Drop rows with missing values
df_cleaned = df.dropna()

# Convert a column to uppercase (e.g., 'name' column)
df_cleaned['name'] = df_cleaned['name'].str.upper()

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)

print("Data has been cleaned and saved to 'cleaned_data.csv'.")
