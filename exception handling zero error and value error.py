#PROGRAM TO HANDLE ZeroDivisionError and ValueError
n=int(input())
l=[]
for i in range(0,n):
    x=list(map(str,input().split()))
    l.append(x)
for j in l:
    try:
        print(int(j[0])//int(j[1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
