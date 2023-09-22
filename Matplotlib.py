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

# Plotting many points 
# the points in both apoints and bpoints should be equal "6 values on apoints and 6 values on bpoints"
import matplotlib.pyplot as plt
import numpy as np
apoints = np.array([2,4,6,8,10,12])
bpoints = np.array([12,10,8,6,4,2])
plt.plot(apoints,bpoints)
plt.show()
# plotting only points and not the line
# run the following 6 lines of code separatelty
import matplotlib.pyplot as plt
import numpy as np
apoints = np.array([2,7,6,8,10,4])
bpoints = np.array([12,3,8,6,4,2])
plt.plot(apoints,bpoints)
plt.show()  

# If no x or y points provided then the pyplot will pick the values accordingly starting from 0 untill it matvhes the number of values in the provided 
# run the following 5 lines of code separately
import matplotlib.pyplot as plt
import numpy as np
apoints = np.array([2,7,6,8,10,4]) # the points provided by the pyplot are {0 1 2 3 4 5}
plt.plot(apoints)
plt.show()

# Matplotlib offers the option for markers to mark where specific points intersect
# run the following 6 lines of code separatelty
import matplotlib.pyplot as plt
import numpy as np
apoints = np.array([2,7,6,8,10,4])
bpoints = np.array([12,3,8,6,4,2])
plt.plot(apoints,bpoints)
plt.show()  

# run the following 6 lines of code separatelty
import matplotlib.pyplot as plt
import numpy as np
apoints = np.array([2,7,6,8,10,4])
bpoints = np.array([12,3,8,6,4,2])
plt.plot(apoints,bpoints,'*-.r',ms = 10,mec = "c",mfc = "c") # "mec changes the outline of the marker to cyan"
# "mfc changes the face of the marker into cyan
plt.show()  

# run the following 6 lines of code separatelty
# plotting multiple lines
# Either by writing multple plt.plot functions or including all the lines to be drawn in a single plt.plot function
import matplotlib.pyplot as plt
import numpy as np
apoints = np.array([12,7,3,8,10,4])
bpoints = np.array([2,3,6,2,4,2])
cpoints = np.array([6,7,6,3,0,4])
dpoints = np.array([12,7,1,6,9,2])
epoints = np.array([7,7,6,8,10,4])
fpoints = np.array([1,3,11,6,4,9])
plt.plot(apoints,bpoints,cpoints,dpoints,epoints,fpoints,linewidth = 2) # "mec changes the outline of the marker to red"
# "mfc changes the face of the marker into cyan
plt.show()  

# Run the following 10 lines of code separately
# Giving labels to our ploted axis
# Use the xlabel() and ylabel() to name your plotted "x" and "y" axis
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
