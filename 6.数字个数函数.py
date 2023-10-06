from random import randint
l=[]
print('随机数字列表长度')
lenth=int(input())
print('数字范围(最大值，闭区间)')
Range=int(input())
for i in range (0,lenth):
    l.append(randint(1,Range))

def 数字个数(List):
    print(List)
    result={}
    for i in List:
        if '数字%d个数'%(i) in result:
            result['数字%d个数'%(i)]+=1
        else:
            result['数字%d个数'%(i)]=1
    return result

print(数字个数(l))