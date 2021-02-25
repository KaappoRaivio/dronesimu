import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = [0, 1]
y = [0, 0]
z = [0, 0]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot(x,y,z)

plt.pause(0.5)
line.set_data_3d((0, 0), (1, 0), (0, 0))

plt.show()