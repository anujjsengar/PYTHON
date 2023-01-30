#Find the sum of all the multiples of  or  below .
n=int(input())
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
for j in l:
    s=0
    for k in range(1,j):
        if k%3==0 or k%5==0:
            s=s+k
    print(s)
        
    
