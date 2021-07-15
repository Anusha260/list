list=[1,2,3]
a1=[]
a2=[]
i=1
while i<len(list)-1:
    a1.append(list[i])
    i+=1
a2.append(list[-1])
d=[]
j=0
while j<len(list):
    m1=[a1[j],a1[j+1]]
    m2=[a1[j],a2[j]]
    m3=[a1[j+1],a2[j]]
    d.append(m1)
    d.append(m2)
    d.append(m3)
    j+=1
    break
print(d)
    