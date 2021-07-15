# l1=[1,2,3]
# l2=["a","b","c"]

# x=l1+l2
# print(x)
list=[1,1,1,64,23,64,22,22,22]
a=len(list)
for i in range(a-2):
    if list[i]==list[i+1] and list[i+1]==list[i+2]:
        print(list[i])