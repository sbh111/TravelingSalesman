import numpy as np
import random as rd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from brute import Brute


def update(frame, ax, cities, brute):
    currRoute = brute.update()
    bestRoute = brute.getBestRoute()
    bestDist = brute.getBestDist()

    ax.clear()
    ax.scatter(cities[:, 0], cities[:, 1], cities[:, 2], c='r', s=50)
    if currRoute is not None:
        ax.plot(currRoute[:, 0], currRoute[:, 1], currRoute[:, 2], color='magenta', linestyle='dashed')
    ax.plot(bestRoute[:, 0], bestRoute[:, 1], bestRoute[:, 2], color='blue', linestyle='solid', linewidth=2)


def main(numCities=10, maxDist=100):
    rd.seed()
    cities = [[maxDist * rd.random(), maxDist * rd.random(), maxDist * rd.random()] for i in range(numCities)]
    cities = np.array(cities)
    brute = Brute(cities)

    fig = plt.figure(figsize=(8, 6))
    ax = p3.Axes3D(fig)

    ani = animation.FuncAnimation(fig, update, fargs=(ax, cities, brute), interval=1)
    plt.show()


main(8, 1)
