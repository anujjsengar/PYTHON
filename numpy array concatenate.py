#You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .
import numpy
n=tuple(map(int,input().split()))
l1=[]
for i in range(n[0]):
    x=list(map(int,input().split()))
    l1.append(x)
arr1=numpy.array(l1)
l2=[]
for i in range(n[1]):
    y=list(map(int,input().split()))
    l2.append(y)
arr2=numpy.array(l2)
result=numpy.concatenate((arr1,arr2),axis=0)
print(result)

    
    




