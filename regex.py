# You are given a string .
#Your task is to find out whether  is a valid regex or not.
#.*\+ : Valid regex.
#.*+: Has the error multiple repeat. Hence, it is invalid.
n=int(input())
l=[]
for i in range(n):
    x=str(input())
    l.append(x)
for j in l:
    if j==".*\+":
        print(True)
    else:
        print(False)
    
