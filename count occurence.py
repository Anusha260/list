list=[1,2,2,3,4,4,5,6,6]
d={}
for c in list:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)