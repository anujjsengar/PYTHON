#The prime factors of  are  and .

#What is the largest prime factor of a given number ?
n=int(input())
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
for j in l:
    r=0
    for a in range(2,j+1):
        if j%a==0:
            p=0
            for b in range(2,a):
                if a%b==0:
                    p=p+1
                    break
            if p==0:
                r=a
    print(r)
                
