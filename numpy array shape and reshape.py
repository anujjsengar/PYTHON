import numpy
#You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.
l=list(map(int,input().split()))
print(numpy.array(l).reshape(3,3))


