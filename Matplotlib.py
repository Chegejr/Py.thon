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
# drawing a line without points or markers
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

# Matplotlib offers the option for markers to mark where specific points intersect. Drawing a line with markers or points included
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

# Run the following 13 lines of code separately
# Giving labels to our ploted axis
# Use the xlabel() and ylabel() to name your plotted "x" and "y" axis
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
font1 = {'family':'serif','color':'blue','size':13}
font2 = {'family':'serif','color':'darkred','size':17}
plt.xlabel("Average Pulse",fontdict=font1) # Label for X axis."fontdict" takes in a dictionary containing information of the font
plt.ylabel("Calorie Burnage",fontdict=font1) # Label for Y axis."fontdict" takes in a dictionary containing information of the font
plt.title("Sports Watch",fontdict=font2,loc="right") # Adds a title to our plotted graph and places it to the right
plt.show()

import matplotlib.pyplot as plt
import numpy as np

population = 65000
carOwners = 25000
carPrices = np.array([200,400,600,800,1000,1400,1800,3500,10000,20000,30000])
owners = np.array([3.5,8.5,2.5,1.8,1.67,1.45,1.4,1.2,1.4,0.458,0.884])

plt.title("Car Owners against Car Prices",c = "r")
plt.grid(color = "Green", linestyle = "--")
plt.ylabel("No: of Owners in Millions")
plt.xlabel("Car Prices In Grands")
plt.plot(carPrices,owners,'*-.r',ms = 10,mec = "c",mfc = "c") # "mec changes the outline of the marker to cyan"
# "mfc changes the face of the marker into cyan
plt.show()

# Displaying multiple graphs in a one  using the subplot
# The subplot() function takes three arguments that describes the layout of the figure.
# The layout is organized in rows and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot.
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.subplot(1, 2, 1)# the graph to be plotted wil be of (1) row and (2) columns and this will  be the (1) plot
plt.plot(x,y)
plt.title("Plot 1") # Sets the title of the first sub-graph
plt.grid(color = "Green", linestyle = "--")

x = np.array([3, 6, 8, 11])
y = np.array([4, 8, 3, 7])

plt.subplot(1, 2, 2)# the graph to be plotted wil be of (1) row and (2) columns and this will  be the (2) plot
plt.plot(x,y)
plt.title("Plot 1")# Sets the title of the second sub-graph
plt.grid(color = "Green", linestyle = "--")

plt.suptitle("Father of Graphs",c="r")# Sets the title of the main graph
plt.show()

# We can plot observations inform of dots and not the lines by use of scatter() function
# The scatter() needs to arrays of the same size: one for x axis values and the other for y axis values

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(10,size=10) # Generates 10 random numbers between 0-9
y = np.random.randint(10,size=10)# Generates 10 random numbers between 0-9
colors = np.random.randint(100,size=10)
plt.scatter(x,y,c=colors,cmap='nipy_spectral')
plt.colorbar()

# Its also possible to plot two scatter observations in one figure
# Always remember to put only one line of "plt.show()" when plotting multiple scatter observations in one figure.
# If by chance you happen to put multiple "plt.show()"  then you will end up having multiple figures with single scatter observations
# instead of having them in one figure

a = np.random.randint(10,size=10) # Generates 10 random numbers between 0-9
b = np.random.randint(10,size=10)# Generates 10 random numbers between 0-9
plt.scatter(a,b,c="green")

c = np.random.randint(10,size=10) # Generates 10 random numbers between 0-9
d = np.random.randint(10,size=10)# Generates 10 random numbers between 0-9
plt.scatter(c,d,c="red")

e = np.random.randint(10,size=10) # Generates 10 random numbers between 0-9
f = np.random.randint(10,size=10)# Generates 10 random numbers between 0-9
colors = np.random.randint(10,size=100)
plt.scatter(e,f,c="yellow")

g = np.random.randint(10,size=10) # Generates 10 random numbers between 0-9
h = np.random.randint(10,size=10)# Generates 10 random numbers between 0-9
plt.scatter(g,h,c="blue")

i = np.random.randint(10,size=10) # Generates 10 random numbers between 0-9
j = np.random.randint(10,size=10)# Generates 10 random numbers between 0-9
plt.scatter(i,j,c="black")
plt.show()

#  Using pyplot so far we have seen we can plot graphs, sctter plots and now bar graphs
# the bars can be displayed bothe horizontally or vertically
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Nike","Vans","Jordan","Clarks","Eazzy"])
y = np.random.randint(1000,size=5)
plt.subplot(1, 2, 1)#Using the subplot to plot two graphs in one figure
plt.bar(x,y,color="black",width=0.5)
plt.title("Types of shoes and Number of Users")

a = np.array(["Benzo","Chev","Ferrari","Audi","Jeep"])
b = np.random.randint(10000,size=5)
plt.subplot(1, 2, 2) #Using the subplot to plot two graphs in one figure
plt.bar(a,b,color="red",width=0.5)
plt.title("Types cars and Number of owners")

plt.show()


# Assuming you want the bar graphs to be horizontal, use "plt.barh"
x = np.array(["Benzo","Chev","Ferrari","Audi","Jeep"])
y = np.random.randint(10000,size=5)
plt.barh(x,y,color="green",height=0.5)
plt.title("Types cars and Number of owners")
plt.show()

# Also the pyplot allows us to create histograms 
# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.
# Example: Say you ask for the height of 250 people.
# Lets use nump to generate 250 random heights concentrated around 175, the standard deviation is 10

import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(175,10,250)#The generated heights will be concentrated around 175, a standard deviation of 10, a total of 250 values

plt.hist(x)
plt.show()

#  Using pyplot, we can also draw pie charts 
import numpy as np
import matplotlib.pyplot as plt

y = np.random.randint(100,size=5)
myLabels = np.array(["Maths","Physics","Chemistry","Mechanis","Dynamics"])
myExplode = [0.3,0,0,0,0]
plt.pie(y,labels=myLabels,explode=myExplode)
plt.legend(title="Subjects")
plt.show()
