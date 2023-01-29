import numpy
#You are given a X integer array matrix with space separated elements ( = rows and  = columns).
#Your task is to print the transpose and flatten results.
n=tuple(map(int,input().split()))
l=[]
for i in range(0,n[0]):
    x=list(map(int,input().split()))
    l.append(x)
print(numpy.transpose(l))
print(numpy.array(l).reshape(1,n[0]*n[1])[0])
    

