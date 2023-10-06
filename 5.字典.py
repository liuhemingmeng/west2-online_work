d={2301:'张三',2302:'李四',2303:'王五',2304:'刘六'}
a=1
while a==1:
    for i in d:
        a=0
        if i%2==0:
            del d[i]
            a=1
            break
print(d)