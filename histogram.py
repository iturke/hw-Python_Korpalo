#Гістограма нормального розподілу
import matplotlib.pyplot as plt
from numpy import *


data = random.randn(1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.title('Гістограма нормального розподілу')
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.grid(True)
plt.show()