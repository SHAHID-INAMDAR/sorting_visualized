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
ax.scatter(x,y)


for i in range(SIZE):
    for i in range(SIZE):
        current = y[i]
        j = i-1
        while y[j]>current and j>=0:
            y[j+1]=y[j]
            j-=1
        y[j+1] = current

        ax.clear()
        ax.scatter(x,y,s=10,c="red")
        plt.pause(0.000005)

plt.show()