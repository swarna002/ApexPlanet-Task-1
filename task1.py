
import pandas as pd

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")
print(df.head())
print("Dataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nDataset Information:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())

df['City'] = df['City'].fillna('Unknown')

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

# Data types
print("\nData Types Before Cleaning:")
print(df.dtypes)

df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

print("\nData Types After Cleaning:")
print(df.dtypes)

# Verify missing values after date conversion
print("\nMissing Values After Date Conversion:")
print(df.isnull().sum())

print("\nInvalid Dates:")
print(df['Order_Date'].isnull().sum())

print("\nDataset Information:")
df.info()

text_columns = [
    'Gender', 'City', 'Product', 'Category', 'Customer_Name'
]

for col in text_columns:
    df[col] = df[col].str.strip()

df['Gender'] = df['Gender'].str.title()

df['Category'] = df['Category'].str.title()
df['Product'] = df['Product'].str.title()

print("\nText formatting standardized successfully!")

numeric_columns = [
    'Age', 'Quantity', 'Unit_Price', 'Total_Sales'
]

print("\nOutlier Assessment:")

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[col] < lower_limit) |
        (df[col] > upper_limit)
    ]

    print(f"{col}: {len(outliers)} potential outliers")

# Inspect potential Total_Sales outliers
Q1 = df['Total_Sales'].quantile(0.25)
Q3 = df['Total_Sales'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

sales_outliers = df[
    (df['Total_Sales'] < lower_limit) |
    (df['Total_Sales'] > upper_limit)
]

print("\nPotential Total_Sales Outliers:")
print(sales_outliers[
    ['Order_ID', 'Product', 'Quantity',
     'Unit_Price', 'Total_Sales']
])

print("\nTotal potential outliers:", len(sales_outliers))

# Total_Sales calculation
expected_sales = df['Quantity'] * df['Unit_Price']

sales_mismatch = ~(
    (df['Total_Sales'] - expected_sales).abs() < 0.01
)

print("\nSales Calculation Mismatches:")
print(sales_mismatch.sum())

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Final verification
check_df = pd.read_csv("cleaned_dataset.csv")
dictionary_df = pd.read_csv("data_dictionary.csv")

print("\nCleaned Dataset Shape:", check_df.shape)
print("Dictionary Shape:", dictionary_df.shape)

print("\nMissing Values:")
print(check_df.isnull().sum())

print("\nDictionary Columns:")
print(dictionary_df.columns.tolist())

