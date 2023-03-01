
import pylab

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import proj3d
matplotlib.use('TkAgg')
fig = plt.figure(figsize=(12,10))

class Plotter:
    def __init__(self, x_points, y_points, z_points, labels):
        self.x_points = x_points
        self.y_points = y_points
        self.z_points = z_points
        self.labels = labels

    def _shorten_points(self):
        self.x_points = self.x_points[0]
        self.y_points = self.y_points[0]
        self.z_points = self.z_points[0]

    def draw_line(self, x_start, x_end, y_start, y_end, z_start, z_end):
        self.ax.plot([x_start, x_end], [y_start, y_end], zs=[z_start, z_end])

    def plot(self):
        # self._shorten_points()

        self.ax = plt.axes(projection="3d")



        self.ax.scatter3D(self.x_points, self.y_points, self.z_points, c=self.z_points, cmap='hsv')





        for idx, label in enumerate(self.labels):
            x2, y2, _ = proj3d.proj_transform(self.x_points[idx], self.y_points[idx], self.z_points[idx], self.ax.get_proj())
            label = label[:4]
            pylab.annotate(label, xy=(x2, y2), xytext=(x2, y2), rotation=0,
                                   ha='left')




        # plt.draw()
        plt.show()

    def show(self):
        plt.show()





