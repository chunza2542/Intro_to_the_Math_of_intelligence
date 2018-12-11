from numpy import *

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def average(points):
    total = [0, 0]

    for i in range(0, len(points)):
        total[0] += points[i, 0]
        total[1] += points[i, 1]
    total[0] /= len(points)
    total[1] /= len(points)

    return total

def compute_sxx(points, xa):
    total = 0
    for i in range(0, len(points)):
        total += (points[i, 0] - xa) ** 2
    return total

def compute_sxy(points, xa, ya):
    total = 0
    for i in range(0, len(points)):
        total += (points[i, 0] - xa) * (points[i, 1] - ya)
    return total


def run():
    points = genfromtxt("data.csv", delimiter=",")

    [xa, ya] = average(points)

    sxx = compute_sxx(points, xa)
    sxy = compute_sxy(points, xa, ya)

    b1 = sxy / sxx
    b0 = ya - b1 * xa

    print "Running..."
    print "f(x) = {0} + {1}x, error = {2}".format(b0, b1, compute_error_for_line_given_points(b0, b1, points))
    print "f(48.10504169176825) = {0}".format(b0 + b1 * 48.10504169176825)

if __name__ == '__main__':
    run()
