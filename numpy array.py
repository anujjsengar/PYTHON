import numpy
#The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
#You are given a space separated list of numbers.
#Your task is to print a reversed NumPy array with the element type float.
#
def arrays(arr):
    l=list(arr)
    l.reverse()
    return numpy.array(l,dtype=float)
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
