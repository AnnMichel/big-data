# Big Data Assignment 1

## Dataset
 Our data set is: amazon.csv 

## Docker Setup
1. **Creating a Directory:**
   ```
   mkdir bd-a1/
   ```

2. **Dockerfile:**
   - Base Image: Ubuntu
   - Installed Packages: Python3, Pandas, Numpy, Seaborn, Matplotlib, scikit-learn, Scipy
   - Created Directory: /home/doc-bd-a1/
   - Moved Dataset File

3. **Building the Docker Image:**
   ```
   docker build -t my_image .
   ```

4. **Running the Container:**
   ```
   docker run -it my_image bash
   ```

## Files in Container
1. **load.py:**
```
import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Please provide the file path as an argument.")
    sys.exit(1)

file_path = sys.argv[1]
df = pd.read_csv(file_path)
print(df.head())

```

2. **dpre.py:**
```
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

```


3. **eda.py:**
```
import pandas as pd

data = pd.read_csv('res_dpre.csv')


insight_1 = "Insight 1: Mean value of column rating is {0}".format(data['rating'].mean())
with open('eda-in-1.txt', 'w') as file:
    file.write(insight_1)


insight_2 = "Insight 2: Maximum value in column discounted_price is {0}".format(data['discounted_price'].max())
with open('eda-in-2.txt', 'w') as file:
    file.write(insight_2)


insight_3 = "Insight 3: Number of unique categories in column category is {0}".format(data['category'].nunique())
with open('eda-in-3.txt', 'w') as file:
    file.write(insight_3)

```

4. **vis.py:**
```

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('res_dpre.csv')

# Create the visualization
plt.figure(figsize=(8, 6))
plt.hist(data['rating'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Ratings')
plt.grid(True)

# Save the visualization as vis.png
plt.savefig('vis.png')
  
```

6. **model.py:**
```

import pandas as pd

data = pd.read_csv('res_dpre.csv')


insight_1 = "Insight 1: Mean value of column rating is {0}".format(data['rating'].mean())
with open('eda-in-1.txt', 'w') as file:
    file.write(insight_1)


insight_2 = "Insight 2: Maximum value in column discounted_price is {0}".format(data['discounted_price'].max())
with open('eda-in-2.txt', 'w') as file:
    file.write(insight_2)


insight_3 = "Insight 3: Number of unique categories in column category is {0}".format(data['category'].nunique())
with open('eda-in-3.txt', 'w') as file:
    file.write(insight_3)

```

6. **final.sh:**

```
# Copy output files from container to local machine
docker cp bd-a1-container2:/home/doc-bd-a1/res_dpre.csv C:/Users/ann_a/bd-a1/service-result
docker cp bd-a1-container2:/home/doc-bd-a1/eda-in-1.txt C:/Users/ann_a/bd-a1/service-result
docker cp bd-a1-container2:/home/doc-bd-a1/eda-in-2.txt C:/Users/ann_a/bd-a1/service-result
docker cp bd-a1-container2:/home/doc-bd-a1/eda-in-3.txt C:/Users/ann_a/bd-a1/service-result
docker cp bd-a1-container2:/home/doc-bd-a1/k.txt C:/Users/ann_a/bd-a1/service-result
docker cp bd-a1-container2:/home/doc-bd-a1/vis.png C:/Users/ann_a/bd-a1/service-result

# Stop the container
docker stop bd-a1-container2 
```

## Exporting Output Files
**( The Output File appears in separate files named : eda-in-1 ,eda-in-2 ,eda-in-3 , k , res_dpe, vis )**
1. **Copying Files to Local Machine:**
   ```
   docker cp bd-a1-container2:/path/to/files /local/machine/directory
   ```

2. **Stopping the Container:**
   ```
   docker stop bd-a1-container2
   ```




