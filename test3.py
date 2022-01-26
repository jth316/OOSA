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

def minvalu(data, n):
    #print(data) #to see original array as it is random
    x=data[0]
    p=0
    for i in range (1,n):
        if data[i]<x:
            x=data[i]
            p=i
    print(x)
    sortdata.append(x)
    data=np.delete(data, np.where(data == p))
    #print(data1)
    #print(sortdata)

data=np.random.random((5))
print(data)
sortdata=[]
for n in data:
    x=data[0]
    p=0
    for i in range (1,len(data)):
        if data[i]<x:
            x=data[i]
            p=i
    print(x)
    sortdata.append(x)
    data.remove(x)
    #y=np.delete(data, np.where(data==p))
    #print(y)
print(sortdata)

