#use the load_wine function from sklearn.datasets
#Loads the Wine dataset.
#Extracts the features into a NumPy array.
#Calculates the mean, median, and standard deviation for each feature across all samples.
#Prints the results, including the name of each feature for clarity.

from sklearn.datasets import load_wine
import numpy as np

wine_data = load_wine()

features = wine_data.data
target = wine_data.target

means = np.mean(features, axis=0)
medians = np.median(features, axis=0)
std_devs = np.std(features, axis=0)

print("Feature names:", wine_data.feature_names)
print("\nMeans of each feature:")
for name, mean in zip(wine_data.feature_names, means):
    print(f"{name}: {mean}")

print("\nMedians of each feature:")
for name, median in zip(wine_data.feature_names, medians):
    print(f"{name}: {median}")

print("\nStandard deviations of each feature:")
for name, std in zip(wine_data.feature_names, std_devs):
    print(f"{name}: {std}")

