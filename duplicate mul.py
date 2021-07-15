list=[1,6,3,6,3,5,1]
a=[]
i=1
mul=1
while i<len(list):
    if list[i] not in a:
        a.append(list[i]) 
        mul=mul*list[i]
    i=i+1
print(mul)
