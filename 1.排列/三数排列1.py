print('输入数字三次')
a=(input())
b=(input())
c=(input())
if a<b:
    if b<c:
        print(c)
        print(b)
        print(a)
    else:
        if a<c:
            print(b)
            print(c)
            print(a)
        else:
            print(b)
            print(a)
            print(c)
else:
    if a<c:
        print(c)
        print(a)
        print(b)
    else:
        if b<c:
            print(a)
            print(c)
            print(b)
        else:
            print(a)
            print(b)
            print(c)