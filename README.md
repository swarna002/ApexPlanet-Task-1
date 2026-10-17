# ApexPlanet Data Analytics Internship — Task 1
This is my first task at ApexPlanet.
## Data Immersion & Wrangling

### Objective
From the supplied sales dataset, document its fields, assess data quality, clean identified issues, and produce an analysis-ready dataset.

### Source dataset
- File: "ApexPlanet_DataAnalytics_Dataset.xlsx"
- Sheet: 'Sales_Dataset'
- Rows: 1,000
- Columns: 12
- Exact duplicate rows: 0
- Missing Age values: 20
- Missing City values: 13
- Rows with a repeated Order_ID: 9

### Cleaning performed
1. Trimmed leading/trailing whitespace from text fields.
2. Standardized capitalization for Gender, City, Product, and Category.
3. Converted `Order_Date` to a proper date field.
4. Filled missing `Age` values with the source median (41 years).
5. Replaced missing `City` values with `Unknown` rather than guessing the city.
6. Found repeated source `Order_ID` values. To avoid deleting distinct-looking transactions, retained the original ID in `Original_Order_ID` and assigned `_DUP01`, `_DUP02`, etc. to later occurrences. These records should be verified with the internship mentor/source owner.
7. Checked `Total_Sales = Quantity × Unit_Price`; all source rows passed the check within 0.02 rounding tolerance.
8. Did not automatically delete statistical outliers. Extreme values should be validated against business context before removal.