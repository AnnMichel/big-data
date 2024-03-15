import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Please provide the file path as an argument.")
    sys.exit(1)

file_path = sys.argv[1]
df = pd.read_csv(file_path)
print(df.head())
