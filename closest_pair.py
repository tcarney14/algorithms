import numpy as np
import math
import matplotlib.pyplot as plt
import random

def closest_pair_brute(points):
    min_dist = np.Inf
    close_pair = ()
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if dist < min_dist:
                min_dist = dist
                close_pair = (points[i], points[j])

    return close_pair


def plot_closest_pair(pair, points):
    points = zip(*points)
    plt.scatter(points[0], points[1])

    pair = zip(*pair)
    plt.plot(pair[0],pair[1])

    plt.show()


if __name__ == "__main__":
    points = set()
    for i in range(20):
        points.add((random.randint(0,50), random.randint(0,50)))
    
    points = list(points)
    close_pair = closest_pair_brute(points)
    print(close_pair)

    plot_closest_pair(close_pair, points)