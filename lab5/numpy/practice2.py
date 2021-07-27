import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])

print(a.size)
print(a.ndim)
print(a.shape)

b = np.array([1, -1, 1, -1])

mean = b.mean()
print(mean)

standard_deviation=a.std()
print(standard_deviation)

print(np.pi)

x = np.array([0, np.pi/2 , np.pi])
y = np.sin(x)
print(y)

linspace = np.linspace(-2, 2, num=3)
print(linspace)
