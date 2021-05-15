import matplotlib.pyplot as plt
import numpy as np
import time


class plotter:
    def __init__(self):
        plt.ion()

        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.ln, = self.ax.plot([], [], 'ro-')

    def update(self):

        time.sleep(0.5)

        xdata = np.arange(10)
        ydata = np.random.random(10)

        self.ln.set_xdata(xdata)
        self.ln.set_ydata(ydata)

        self.ax.relim()
        self.ax.autoscale_view()

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()