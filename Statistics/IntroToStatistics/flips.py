
import random

from math import sqrt

def mean(data):
    return sum(data) / len(data)

def variance(data):
    return sum([(i - mean(data)) ** 2 for i in data]) / len(data)

# standard deviation
def stddev(data):
    return sqrt(variance(data))

def flip(N):
    return [1 if random.random() > 0.5 else 0 for _ in range(N)]


if __name__ == '__main__':
    N = 1000
    f = flip(N)

    print(mean(f))
    print(stddev(f))
