#Стовпчикова діаграма
import matplotlib.pyplot as plt

categories = ['1', '2', '3', '4']
values = [23, 45, 12, 30]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=['pink', 'cyan', 'linen', 'coral'])
plt.title('Стовпчаста діаграма')
plt.xlabel('Категорії')
plt.ylabel('Значення')
plt.show()