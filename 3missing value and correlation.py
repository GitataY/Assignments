import pandas as pd
import numpy as np

# Fetch the dataset from the original source
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# Since the dataset is split across rows, we need to rearrange it properly
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# Convert the data into a pandas DataFrame
feature_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]
boston_df = pd.DataFrame(data, columns=feature_names)

# Add the target variable to the DataFrame
boston_df["MEDV"] = target

# Check for missing values in the DataFrame
missing_values = boston_df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Calculate the correlation matrix
correlation_matrix = boston_df.corr()

# Display the correlation matrix
print("\nCorrelation matrix:")
print(correlation_matrix)
