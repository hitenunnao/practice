# how to take users input into the list

# step 1: creating an empty list
# step 2: number of elemments
# step 3: iterating it
# step 4:adding the element by "list_name.append(var_name)"

l1=[]
n=int(input("enter the numbber of elements"))
for i in range(0,n):
    element=int(input())
    l1.append(element)
print(l1)

l2=[]
n=int(input("enter the numbber of elements"))                      
i=1
while(i<=n):
    element=input("dal bsdk")
    l2.append(element)
    i=i+1
print(l2)