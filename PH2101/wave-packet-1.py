import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

L = 50;
v = 10;

xs = np.linspace(0, L, num=2000, endpoint=True);

k1 = 2*np.pi/200;
k2 = 2*np.pi/4;

ks = np.linspace(k1, k2, num=2000, endpoint=True);

ws = v*ks # .+ 1*ks.^3;
ts = np.arange(0.0, L/v, 0.01);
num_frame = len(ts)

t = ts[0];
ys = 2000*[0.0];
for i in range(2000):
    ys = ys + np.cos(ks[i]*xs - ws[i]*t);
myline = ax.plot(xs, ys)

def update_plot(frame):
    ys = 2000*[0.0];
    t = ts[frame]
    for i in range(2000):
        ys = ys + np.cos(ks[i]*xs - ws[i]*t);
    
    myline[0].set_xdata(xs)
    myline[0].set_ydata(ys)
    return myline

ani = animation.FuncAnimation(fig = fig, func = update_plot, frames = num_frame, interval = 30)

# The following line saves the animation. You must have ffmpeg to convert your animation
# to a movie form (gif, mp4 etc). You may use other *writers* to do this. Please check
# animation documentation.
#ani.save(filename='wave-package-1-move.gif', writer='ffmpeg')

plt.show()
