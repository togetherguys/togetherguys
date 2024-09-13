result=[]
for i in range(101,201):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        result.append(i)
print(len(set(result)))
print(sorted(list(set(result)),reverse=False))    #此处进行过修改。
