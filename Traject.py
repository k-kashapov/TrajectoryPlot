#!/usr/bin/python3

import matplotlib.pyplot as plt
import random
import math

draw_arrows: bool = True

if draw_arrows:
    print("Drawing arrows ON")
    from matplotlib.patches import FancyArrowPatch, PathPatch
    from matplotlib.path import Path
    arrow_width = 2.
    arrowstyle = "fancy,head_length={},head_width={},tail_width={}".format(2 * arrow_width, 3 * arrow_width, arrow_width)

print("Imported libs")

# Length of a single trajectory line in steps
length:    int = int(1e4)

# Maximum distance between (0, 0) and x(0), y(0)
delta:     float = 1.5

# Number of trajectories to calculate
n_points:  int   = 200

# Distance from (0, 0) at which the calculation should stop
radius:    float = 4.0

# Step in time between recalculations
timeStep = 1e-4

# Add dx and dy to x, y with respect to timeStep
def getNextPos(x, y, funcX, funcY) -> float:
    return (x + funcX(x, y) * timeStep, y + funcY(x, y) * timeStep)

# dx/dt
def dxdt(x, y) -> float:
    return y

# dy/dt
def dydt(x, y) -> float:
    return x - x * x

print("Calculating...")

# Calculate single trajectory
# IN:  curr_x, curr_y = trajectory start point
# OUT: (xs, ys) - points of the trajectory
def getTraject(curr_x, curr_y):
    xs = [curr_x]
    ys = [curr_y]

    for i in range(length):
        new_x, new_y = getNextPos(curr_x, curr_y, dxdt, dydt)
        
        if (abs(new_x) > radius or abs(new_y) > radius):
            break
        
        xs.append(new_x)
        ys.append(new_y)
        
        curr_x = new_x
        curr_y = new_y

    return (xs, ys)

try:
    fig, ax = plt.subplots(1, 1)
    
    for j in range(0, n_points):
        print("\r", j + 1, "/", n_points, end="")

        curr_x = (random.random() * 2 - 1) * delta
        curr_y = (random.random() * 2 - 1) * delta

        xs, ys = getTraject(curr_x, curr_y)

        if (draw_arrows):
            posA, posB = zip(xs[-2:], ys[-2:])
            arrow = FancyArrowPatch(posA=posA, posB=posB, arrowstyle=arrowstyle, color='k')
            ax.add_artist(arrow)        

        ax.plot(xs, ys)
finally:
    print("\nPlotting...")
    plt.show()
    print("Stop")
