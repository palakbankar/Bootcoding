import matplotlib.pyplot as plt
fruit = ['apple','banana','orange']
sales = [100,200,150]

plt.bar(fruit,sales)
plt.xlabel('Fruit')
plt.ylabel('Sales')
plt.show()