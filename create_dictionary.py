import pandas as pd

data = [
    ["Order_ID", "str", "Unique order identifier", "Track individual orders"],
    ["Order_Date", "datetime", "Date of order", "Analyze sales trends"],
    ["Customer_ID", "str", "Unique customer identifier", "Customer analysis"],
    ["Customer_Name", "str", "Customer name", "Identify customer records"],
    ["Age", "float", "Customer age", "Age-group analysis"],
    ["Gender", "str", "Customer gender", "Demographic analysis"],
    ["City", "str", "Customer city", "Location-wise sales"],
    ["Product", "str", "Product name", "Product performance"],
    ["Category", "str", "Product category", "Category-wise sales"],
    ["Quantity", "int", "Units ordered", "Analyze sales volume"],
    ["Unit_Price", "float", "Price per unit", "Pricing analysis"],
    ["Total_Sales", "float", "Total sales value per record", "Revenue analysis"]
]

columns = [
    "Variable",
    "Data_Type",
    "Meaning",
    "Business_Relevance"
]

dictionary = pd.DataFrame(data, columns=columns)
dictionary.to_csv("data_dictionary.csv", index=False)

print("Data dictionary saved successfully!")
