# Create a NumPy array of shape (3, 4) with random integers between 0 and 9
# Print the array
# Calculate the mean of the array
# Print the mean

import numpy as np

array = np.random.randint(0, 10, (3, 4))

print("Array:\n", array)

mean_value = array.mean()

print("Mean of the array:", mean_value)