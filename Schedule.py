import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(-5, 5, 100)
y = x ** 2 + 5 * np.sin(x)
x1 = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
#y = x ** 2
#y = np.sin(x)

#y = np.exp(x)
ax.plot(x, y,
        marker = ',',
        markersize = 6,
        linestyle = 'dashdot',
        linewidth = 3,
        color = 'r')
ax.plot(x1, y1,
        marker = 'h',
        color = 'b')
plt.xlabel('Day', fontsize=12, color='blue')
plt.ylabel('Price', fontsize=12, color='blue')
plt.grid()
plt.show()