s=input('输入字符串\n')
length=len(s)
l=[]
before=''
for i in range(0,length):
    now=s[i]
    after=s[i:i+2]
    if i!=0:
        before=s[i-1:i+1]#前读取框
    if after=='ol':
        l.append('fzu')
    elif before!='ol':
        l.append(now)
print(l)
'''
替换可以直接用print(s.replace('ol','fzu'))
'''
l=(list(''.join(l)))
newlength=len(l)
newl=[]
for i in range(1,newlength+1):
    newl.append(l[0-i])
print(''.join(newl))
'''
直接用str[::-1]即可#字符串倒序
或''.join(l.reverse)#列表倒序
'''