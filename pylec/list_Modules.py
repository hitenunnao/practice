l=[34,45,77,64,2,47]
l1=[12,107,78]
l.append(23)        #1
print(l)
l.sort()            #2
print(l)
l.reverse()         #3
print(l)
l2:list[str]=l.copy()           #4
print(l2)
l.reverse()         #5
l.extend(l1)
print(l)
l.remove(45)        #6
print(l)
y=l.index(23)       #7
print(y)
l[y]=32     
print(l)
print(l.count(45))  #8
z=l.pop(0)          #9
print(z)
print(l)
l.clear()           #10
print(l)