import pandas as pd


df = pd.read_csv('amazon.csv')

df.describe()

# Data Cleaning
# Task 1: Remove any duplicate rows
df = df.drop_duplicates()

# Task 2: Remove any missing values
df = df.dropna()

# Data Transformation
# Task 1: Convert the 'discounted_price' and 'actual_price' columns to numeric
df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)

# Task 2: Extract the brand name from the 'product_name' column
df['brand'] = df['product_name'].str.split(' ').str[0]

# Data Reduction
# Task 1: Keep only the relevant columns for analysis
df = df[['product_id', 'product_name', 'category', 'discounted_price', 'actual_price', 'rating', 'rating_count']]

# Convert 'rating' column to numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# Filter out low-rated products (rating less than 4.0)
df = df[df['rating'] >= 4.0]

# Data Discretization
# Task 1: Create bins for 'discounted_price' column
bins = [0, 25, 50, 75, 100]
labels = ['0-24%', '25-49%', '50-74%', '75-100%']
df['discount_range'] = pd.cut(df['discounted_price'], bins=bins, labels=labels)

# Task 2: Convert 'rating_count' column to categorical variable
df['rating_count'] = pd.qcut(df['rating_count'], q=3, labels=['Low', 'Medium', 'High'])

# Save the resulting dataframe as a new CSV file
df.to_csv('res_dpre.csv', index=False)
