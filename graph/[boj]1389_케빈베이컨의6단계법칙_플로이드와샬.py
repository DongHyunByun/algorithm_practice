N,M=map(int,input().split())
maxNum=9876543210
L=[[maxNum for j in range(N+1)] for i in range(N+1)]

for i in range(1,M+1):
    a,b=map(int,input().split())
    L[a][b]=1
    L[b][a]=1
for i in range(1,N+1):
    L[i][i]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            temp=L[i][k] + L[k][j]
            if L[i][j]>temp:
                L[i][j]=temp

ansNum=maxNum
ans=0
for i in range(1,N+1):
    tempSum=sum(L[i][1:])
    if tempSum<ansNum:
        ansNum=tempSum
        ans=i
print(ans)