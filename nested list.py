#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
n=int(input())
l=[]
for i in range(0,n*2):
    x=str(input())
    l.append(x)
a=[]
for j in range(1,n*2,2):
    a.append(float(l[j]))
a.remove(min(a))
for y in range(l.count(min(a))):
    print(l[l.index(str(min(a)))-1])
    
    
    
        
        
    
