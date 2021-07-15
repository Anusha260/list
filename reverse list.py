n=int(input("enter num"))
rev=1
i=1
b=[]
while i<=n:
    a=n%10
    rev=(rev*10)+a
    n=n//10
    b.append(a)
print(b)
i=i+1