# Matplotlib is a python library that provides data visualization
# It a low level library
# Install matplotlib using "pip install matplotlib"
import matplotlib
import matplotlib.pyplot as plt
print(matplotlib.__version__) # Output------> 3.8.0
import numpy as np

# Plot a line with the following coordinates {6,250} starting from the origin
xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()

"""
Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

"""
wpoints = np.array([1,8])
zpoints = np.array([3,10])
plt.plot(wpoints,zpoints)
plt.show()
