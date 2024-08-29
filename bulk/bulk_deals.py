import pandas as pd

# Load the data from a CSV file
data = pd.read_csv('bulk_deals.csv')

# 1. Calculate the % increase of bulk price compared to discount price
data['% Bulk Price Premium'] = ((data['bulk_price'] - data['discount_price']) / data['discount_price']) * 100

# 2. Calculate the buying price (0.3% above the bulk price) and selling price (0.5% below the high price)
data['Buying Price'] = data['bulk_price'] * 1.003
data['Selling Price'] = data['high'] * 0.995

# 3. Calculate the gains percent according to buying and selling price
data['Gains %'] = ((data['Selling Price'] - data['Buying Price']) / data['Buying Price']) * 100

# 4. Calculate how much % up the buying price is from the discount price
data['% Up Buying vs Discount'] = ((data['Buying Price'] - data['discount_price']) / data['discount_price']) * 100

# 5. Round the results to 2 decimal places
data = data.round({'% Bulk Price Premium': 2, 'Buying Price': 2, 'Selling Price': 2, 
                   'Gains %': 2, '% Up Buying vs Discount': 2})

# Display the final DataFrame
print(data)

# Optional: Save the results to a new CSV file
data.to_csv('processed_stock_data.csv', index=False)

# Select only the specified columns
filtered_data = data[['date', 'stock', 'seller', 'exchange', '% Up Buying vs Discount', 'Gains %', 'open_mkt']]

# Convert the DataFrame to an HTML table
html_table = filtered_data.to_html(index=False)

# Save the HTML table to a file
with open('stock_data.html', 'w') as file:
    file.write(html_table)

# # Create the HTML content with a link to the external CSS file
# html_content = f'''
# <html>
# <head>
# <link rel="stylesheet" type="text/css" href="styles.css">
# </head>
# <body>
# {html_table}
# </body>
# </html>
# '''


print("HTML table successfully created and saved as 'stock_data.html'")