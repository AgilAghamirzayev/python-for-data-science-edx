import time
import sys

import numpy as np

import matplotlib.pyplot as plt

def Plotvec1(u, z, v):
    ax = plt.axes()

    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')

    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


def Plotvec2(a, b):
    ax = plt.axes()

    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')

    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')

    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


a = np.array([0, 1, 2, 3, 4, 5])
print(a)

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(type(a))
print(a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
print(b.dtype)


u = np.array([1, 0])
v = np.array([0, 1])

z = u + v
print(z)

Plotvec1(u, z, v)


x = np.linspace(0, 2*np.pi, num=100)

y = np.sin(x)

plot = plt.plot(x, y)
