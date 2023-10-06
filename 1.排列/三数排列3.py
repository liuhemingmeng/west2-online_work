l=[int(input()),int(input()),int(input())]
while c==0:
    c=0
    for i in range(len(l)):
        if i<len(l)-1:
            if l[i]<l[i+1]:
                a=l[i]
                b=l[i+1]
                l[i]=b
                l[i+1]=a
                break
        else:
            c=1
print(l)
