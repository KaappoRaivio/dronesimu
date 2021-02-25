from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

from src.drone import Drone
from src.vector import Vector3D, PositionalVector3D



drone = Drone()
fig = pyplot.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection="3d")

line, = ax.plot(*drone.getPlottable())



def update(frame):
    drone.tick(0.01, Vector3D(0, 0, -9.81))
    line.set_data_3d(*drone.getPlottable())
    fig.gca().relim()
    # fig.gca().autoscale_view()
    return line,


animation = FuncAnimation(fig, update, interval=10, blit=True)

# pyplot.ion()
pyplot.xlim((-25, 25))
pyplot.ylim((-25, 25))
ax.set_zlim((0, 50))
pyplot.show()