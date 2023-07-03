from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# initializing a figure in
# which the graph will be plotted
fig = plt.figure()

# marking the x-axis and y-axis
axis = plt.axes(xlim=(0, 400), ylim=(0,400))
def gen_random_points(count,min=0,max=1000):
    t = []
    for i in range(count):
        t.append([np.random.randint(min,max +1) for _ in range(2)])
    return t 
points = gen_random_points(300, 0,400)
x_values = [point[0] for point in points ]
y_values = [point[1] for point in points ]
# initializing a line variable
(points_scatter,) = axis.plot(x_values, y_values)

# data which the line will
# contain (x, y)
def init():
    return (points_scatter,)


def animate(i):
    points = gen_random_points(300, 0,400)
    x_values = [point[0] for point in points ]
    y_values = [point[1] for point in points ]
    points_scatter.set_data(x_values , y_values)
    return [points_scatter]


anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

anim.save("./continuousSineWave.mp4", writer="ffmpeg", fps=30)
