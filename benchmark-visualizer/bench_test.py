import util.general_helper.general_helper as H

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
x = [1,2,3]
y = [1,2,3]
z = [1,2,3]

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
ax.grid()

ax.scatter(x, y, z, c = 'r', s = 50)
ax.set_title('3D Scatter Plot')

# Set axes label
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

plt.show()