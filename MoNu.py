
str='MoNa'
i=0
while i<len(str):
    if ord(str[i])>=65 and ord(str[i])<=90:
        a=ord(str[i])+32
        print(chr(a),end="")
    else:
        b=ord(str[i])-32
        print(chr(b),end="")
    i+=1