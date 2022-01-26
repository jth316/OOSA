import numpy as np

def minvalu(n):
    #print(data) #to see original array as it is random
    x=data[0]
    for i in range (1,n):
        if data[i]<x:
            x=data[i]
    print(x)
    sortdata.append(x)
    Y=np.delete(data, 1)
    #print(data1)
    #print(sortdata)

data=np.random.random((5))
print(data)
sortdata=[]
minvalu(5)
print(sortdata)
print(Y)





