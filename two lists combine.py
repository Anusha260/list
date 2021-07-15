a=[1,2,3]
b=[4,5,6]
d=[]
i=0
while i<len(a):
    j=0
    while j<len(a):
        c=(a[i],b[j])
        d.append(c)
    print(d)
    i=i+1
