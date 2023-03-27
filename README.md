# TrajectoryPlot
Plots the solutions of differential equation in Python. Finds numerical solution with given time step. Trajectory starting points are picked randomly in a square of a given size.

## Setup
Set `draw_arrows` to `True` if you want arrows to be drawn at the end of the line. Arrow's direction corresponds with trajectory's.

Some other parameters listed in program text can be changed. Give it a try.

## Usage
Run `Trajectory.py` in python3 or bash.

## Examples

1) `dx/dt = y, dy/dt = x - x^2`

![Figure_1](https://user-images.githubusercontent.com/52855633/227819813-4666d391-8790-43e4-ad66-def81e0e5421.png)

2) `dx/dt = y + 100x * sqrt(x^2 + y^2),  dy/dt = -x + 100y * sqrt(x^2 + y^2)`

![spirals](https://user-images.githubusercontent.com/52855633/227819956-848d221e-2594-41c7-bf38-2b99b11feaaf.png)

3) Calculation log
```
$ ./Traject.py
Drawing arrows ON
Imported libs
Calculating...
 200 / 200
Plotting...
Stop
```
