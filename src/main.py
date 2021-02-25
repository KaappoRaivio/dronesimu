import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

line = ax.quiver([0], [0], [0], [0.1], [0], [0])
for i in range(100):
    line.set_segments(([0], [0], [0], [0.1], [0], [0]))
    print(line)
    plt.pause(0.01)
    plt.draw()
    plt.cla()


# plt.show()
