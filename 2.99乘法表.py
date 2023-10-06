a=1
b=1
print('%d*%d=%d'%(a,b,a*b),end=(''))
while a<9:
    if a<b:
        a+=1
        print('%d*%d=%d'%(a,b,a*b),end=(''))
        print('  ',end=(''))
    else:
        print()
        a=1
        b+=1
        print('%d*%d=%d'%(a,b,a*b),end=(''))
        print('  ',end=(''))