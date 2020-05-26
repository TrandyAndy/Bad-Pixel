import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 1000)  # Create a list of evenly-spaced numbers over the range
y = np.linspace(0, 20 ,1000)
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.plot(y, np.cos(y))
plt.show()                   # Display the plot
z = 100
if z>10:
    print("Jo")
else:
    print("No")
