def pal(n):
    return str(n) == str(n)[::-1]
p=int(input())
a=" tr"+str(p)+"ue"
b=" fal"+str(p)+"se"
if pal(p):
    print(a)
else:
    print(b)
