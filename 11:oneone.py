list=[21,22,54]
i=0
d={}
while i<len(list):
    s=str(list[i])
    j=0
    string=""
    while j<len(s):
        if s[j]=="1":
            string+="one"
        elif s[j]=="2":
            string+="two"
        elif s[j]=="3":
            string+="three"
        elif s[j]=="4":
            string+="four"
        elif s[j]=="5":
            string+="five"
        j=j+1
    d[list[i]]=string
    i=i+1
print(d)


