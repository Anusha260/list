# a=['apple',"banana"]
# b=['apple',"banana"]
# print(b is not a)
# print(id(a))
# print(id(b))
l=["s_hailu","a_nusha"]
a=[]
i=0
while i<len(l):
    j=0
    s=""
    while j<len(l[i]):
        if l[i][j]=="_":
            pass
        else:
            s=s+l[i][j]
        j=j+1
    # a.append(s)
    i=i+1
    a.append(s)
print(a)
