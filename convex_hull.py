import matplotlib.pyplot as plt
import numpy as np
import itertools

def convex_hull(points):
    x_min = np.Inf, 0
    y_min = 0, np.Inf

    x_max = np.NINF, 0
    y_max = 0, np.NINF

    for point in points:
        if point[0] < x_min[0]:
            x_min = point

        if point[0] > x_max[0]:
            x_max = point

        if point[1] < y_min[1]:
            y_min = point
        
        if point[1] > y_max[1]:
            y_max = point
    
    return [x_min, x_max, y_min, y_max]

def convex_hull_brute(points):
    hull = []
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            a = y2 - y1
            b = x1 - x2
            c = x1*y2 - x2*y1

            signs = []
            for k in range(len(points)):
                x, y = points[k]
                sign = a*x + b*y - c
                if sign > 0:
                    signs.append(True)
                elif sign < 0:
                    signs.append(False)
            
            # Result from count matches with result from len()
            in_hull = signs.count(signs[0]) == len(signs)
            if in_hull:
                hull.append((points[i], points[j]))
    
    return hull

def plot_hull(points, hull):
    points = zip(*points)
    plt.scatter(points[0], points[1])
    
    for line in hull:
        xs, ys = zip(*line)
        plt.plot(xs, ys)

    plt.xlim((0, 10))
    plt.ylim((0, 10))
    plt.show()

if __name__ == "__main__":
    points = [(4, 6), (3, 2), (6,6), (6,1), (2,9), (3, 7), (5, 3)]

    hull = convex_hull_brute(points)
    print(hull)
    plot_hull(points, hull)