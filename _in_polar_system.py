#Графіки в полярній системі координат
import matplotlib.pyplot as plt
from numpy import *

theta = linspace(0, 2 * pi, 1000)
r = exp(sin(theta)) - 2*cos(4*theta)
r2 = theta / (2 * pi)

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, color='green')
ax.plot(theta, r2, label='r = θ / 2π', color='orange', linestyle='dashed')
ax.set_title('Комбінований полярний графік', va='bottom')
ax.legend(loc='lower right')
plt.show()