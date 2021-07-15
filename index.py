list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
a=[]
while i<len(list):
    j=0
    while j<len(list):
        if list[i][j] not in a:
            a.append(list[i][j])
        j=j+1
    i=i+1
print(a)