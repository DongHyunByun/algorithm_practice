n,m=map(int,input().split())

def cntNum(a,num):
    ans=0
    multiNum=num
    while(multiNum<=a):
        ans+=a//multiNum
        multiNum*=num
    return ans

a=cntNum(n,5)
b=cntNum(m,5)
c=cntNum(n-m,5)
five=a-b-c

a=cntNum(n,2)
b=cntNum(m,2)
c=cntNum(n-m,2)
two=a-b-c

print(min(five,two))


