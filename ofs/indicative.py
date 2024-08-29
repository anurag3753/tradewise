"""
URLS:

BSE: https://www.bseindia.com/markets/PublicIssues/OFSIssuse_new.aspx
NSE: https://www.nseindia.com/market-data/public-issues-offer-for-sale-ofs
"""

TOTAL_HNI = 46296296     # base
# TOTAL_HNI = 120370370  # with oversubcription (green shoe)
# TOTAL_RETAIL = 13374486

import pandas as pd

def read_data():
    # Define the path to your Excel file
    excel_file_path = 'combined.xlsx'
    
    # Read the Excel file into a pandas DataFrame
    try:
        df = pd.read_excel(excel_file_path, engine='openpyxl')
    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return None
    
    # Remove commas from the numeric columns and convert them to the appropriate numeric type
    for col in df.columns:
        if df[col].dtype == object:
            # Replace dashes with NaN and remove commas
            df[col] = df[col].replace({'-': pd.NA, ',': ''}, regex=True)
            # Convert columns to numeric, setting non-convertible values to NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Handle NaN values if necessary (e.g., fill with 0 or drop rows/columns)
    # df.fillna(0, inplace=True)  # Example: Fill NaNs with 0

    return df

# Now you have a DataFrame with numbers adjusted properly
df_bse = read_data()

# If you need to sort the DataFrame by 'Price Interval' in descending order
df_sorted = df_bse.sort_values(by='Price Interval', ascending=False)

# Initialize a running total
total_confirmed = 0

# Iterate through the DataFrame rows in descending order of 'Price Interval'
for index, row in df_sorted.iterrows():
    total_confirmed += row['Total']
    subscription_percent = (total_confirmed / TOTAL_HNI) * 100
    if total_confirmed >= TOTAL_HNI:
        # Found the price at which it is fully subscribed
        fully_subscribed_price = row['Price Interval']
        print("Fully subscribed at price interval:", fully_subscribed_price)
        print(f"Current subscription percentage: {subscription_percent:.2f}%")
        print("--------------------------------------------------------------")
        # Determine the next higher bid price (assuming a minimum increment)
        next_higher_bid = fully_subscribed_price + 0.05  # Replace 0.05 with the actual increment
        print("Next higher bid should be:", next_higher_bid)

        estimated_bid = round(fully_subscribed_price * 1.005, 2)   # 0.05% higher than latest estimate available
        print("Estimated higher bid should be:", estimated_bid)
        break
else:
    print("Not fully subscribed within the given data.")
    print(f"Current subscription percentage: {subscription_percent:.2f}%")
