import matplotlib.pyplot as plt
import random

x = [a for a in range(50, 100)]
index = [2, 12, 20, 25, 30, 35, 40, 45]
for i in index:
    x[i] = 0

y1 = []
y2 = []
for i in range(len(x)):
    lst1 = [a*(100-i) for i, a in enumerate(x[:i+1][::-1])]
    lst1_weight = [100-i for i in range(len(x[:i+1]))]
    y1.append(sum(lst1)/sum(lst1_weight))

    lst2 = [a*(i+1) for i, a in enumerate(x[:i+1])]
    lst2_weight = [i+1 for i in range(len(x[:i+1]))]
    y2.append(sum(lst2)/sum(lst2_weight))

plt.plot(x, y1, color='green')
plt.plot(x, y2, color='orange')
plt.show()
