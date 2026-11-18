import matplotlib.pyplot as plt
import random

SIZE = 100
x=[]
y=[]

for i in range(SIZE):
    x.append(i)
    y.append(i)

random.shuffle(y)

fig ,ax =plt.subplots()
ax.scatter(x,y,s=10 ,c="red")

for i in range(SIZE):
    for i in range(SIZE - 1):
        mini = i
        for j in range(i + 1, SIZE):
            if y[j] < y[mini]:
                mini = j
        y[i],y[mini] = y[mini],y[i]
        ax.clear()
        ax.scatter(x,y, s =10 , c= "red")
        plt.pause(0.000005)

plt.show()