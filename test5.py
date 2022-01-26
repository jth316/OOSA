import numpy as np

data=np.random.random((5))
sortdata=[]
print(data)
while len(data)>0:
    x=data[0]
    for i in range (1,len(data)):
        if data[i]<x:
            x=data[i]
    print(x)
    sortdata.append(x)
    data = np.delete(data, np.where(data == x))
print(sortdata)
print(data)


