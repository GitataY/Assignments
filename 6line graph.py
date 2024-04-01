# Generate a range of values from -2π to 2π
# Calculate the sine and cosine of these values
# Create the plot
# Customize the plot
# Display the plot


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')

plt.title('Sine and Cosine Functions') 
plt.xlabel('x values')  
plt.ylabel('y values') 
plt.legend() 

plt.show()
