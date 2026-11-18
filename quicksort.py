import matplotlib.pyplot as plt
import random

def partition(y,l,h):
    pivot = y[h]
    i = l-1
    for j in range(l,h):
        if y[j]<pivot:
            i+=1
            y[i],y[j] = y[j],y[i]
            ax.clear()
            ax.scatter(x,y ,s=10 , c="red")
            plt.pause(0.000005)
    y[i+1],y[h] = y[h],y[i+1]
    return i+1

def quicksort(y,l,h):
    if l<h:
        p =partition(y,l,h)
        quicksort(y,l,p-1)
        quicksort(y,p+1,h)


SIZE = 100
x=[]
y=[]

for i in range(SIZE):
    x.append(i)
    y.append(i)

random.shuffle(y)

fig ,ax =plt.subplots()
ax.scatter(x,y)

quicksort(y,0,SIZE-1)

plt.show()