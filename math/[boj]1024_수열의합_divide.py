N,L=map(int,input().split())

l=L
flag=True
while(l<=100):
    temp=N-(1/2)*(l**2)+(1/2)*l
    if temp<0:
        break
    if temp%l==0:
        x=int(temp//l)
        flag=False
        print(*[x+i for i in range(l)])
        break
    l+=1

if flag:
    print(-1)