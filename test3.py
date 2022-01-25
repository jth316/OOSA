import numpy as np

def randomarray(n):
    data=np.random.random((n))
    print(data)

def minval():
    x=min(np.random.random((10)))
    

def bubblesort(n):
    data=np.random.random((n))
    for i in range (1,n):
        for j in range (0,n-1):
            if data[j]>data[j+1]:
                temp = data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    print(data)

def sort():
    data=np.random.random((5))
    print(data)
    sortdata=np.empty((5))
    x=min(data)
    while len(data)>0:
        sortdata.append('x')
        data.remove('x')
    print(sortdata)

sort()


