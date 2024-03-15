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
