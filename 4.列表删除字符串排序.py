l=[1,'1',4,'5',1,'4']
lenth=len(l)
while a==1:
    a=0
    for i in range(0,lenth):
        if type(l[i])==str:
            del l[i]
            lenth-=1
            a=1
            break
l.sort()
print(l) 