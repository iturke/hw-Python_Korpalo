#Графіки в декартовій системі координат
import matplotlib.pyplot as plt
from numpy import *

x = linspace(-10, 10, 400)
y1 = sin(x)
y2 = cos(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')
plt.title('Графіки sin(x) та cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()