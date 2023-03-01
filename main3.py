import math
import csv
import random
from collections import defaultdict

import matplotlib.pyplot as plt

from plotter import Plotter
from matplotlib.animation import  FuncAnimation

COORDINATES_FILE = "Coordinates.csv"
DISTANCE_FILE  = "distances.csv"
DIJKSTRA = True

x_points = []
y_points = []
z_points = []
stars = []


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 + ( z1 - z2 ) ** 2)



coordinates = {}
adjacency_list = defaultdict(list)



with open(COORDINATES_FILE, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for star_name, x, y, z in reader:
        stars.append(star_name)
        x_points.append(int(x))
        y_points.append(int(y))
        z_points.append((int(z)))
        coordinates[star_name] = (int(x), int(y), int(z))

with open(DISTANCE_FILE, "r") as file:
    reader = csv.reader(file)
    for source, destination, dist in reader:
        adjacency_list[source].append((destination, int(dist)))


SOURCE_STAR = "TRAPPIST-1"
DESTINATION_STAR = "55 Cancri"
# DESTINATION_STAR = "Upsilon Andromedae"
plotter = Plotter(x_points, y_points, z_points, stars)



from heapq import heapify, heappop, heappush
priority_queue = [ (0, SOURCE_STAR, None, 0)  ]
visited = set()
parent_map = {}

def dijkstra_step(i):


    # f_n = g_n + h_n
    if priority_queue:
        key, current_star, parent, path_distance_from_src = heappop(priority_queue)
        # print(f"Popped {current_star}")
        parent_map[current_star] = parent
        if parent != None:
            parent_x, parent_y, parent_z = coordinates[parent]
            dest_x, dest_y, dest_z = coordinates[current_star]
            plotter.draw_line(parent_x, dest_x, parent_y, dest_y, parent_z, dest_z)

        if current_star in visited:
            return
            # continue
        if current_star == DESTINATION_STAR:
            print("Reached " + " " + DESTINATION_STAR + " Distance = " + str(path_distance_from_src) )
            ani.event_source.stop()
            return
        visited.add(current_star)
        for neigborstar_name, neigborstar_distance in adjacency_list[current_star]:

            new_path_distance_from_src = path_distance_from_src + neigborstar_distance

            if DIJKSTRA:
                heappush(priority_queue, (new_path_distance_from_src, neigborstar_name, current_star, new_path_distance_from_src))

            else:
                print(f"From {current_star} to {neigborstar_name} | Distance from src: {new_path_distance_from_src} | Key: {new_path_distance_from_src + distance(*coordinates[neigborstar_name], *coordinates[DESTINATION_STAR])} ")
                heappush(priority_queue, (new_path_distance_from_src + distance(*coordinates[neigborstar_name], *coordinates[DESTINATION_STAR]), neigborstar_name, current_star, new_path_distance_from_src))



ani = FuncAnimation(plt.gcf(), dijkstra_step, interval=100)

plt.tight_layout()
print("Start")
plotter.plot()
print("END")

