INF=9876543210

N=int(input())

L=[[INF for j in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    L[i][i]=0

while(1):
    a,b=map(int,input().split())
    if a==-1:
        break
    L[a][b]=1
    L[b][a]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if L[i][k]+L[k][j]<L[i][j]:
                L[i][j]=L[i][k]+L[k][j]

point=[]
for i,a in enumerate(L[1:]):
    point.append([max(a[1:]),i+1])

score=min(point)[0]
ans=[]
for s,i in point:
    if s==score:
        ans.append(i)
ans.sort()

print(score,len(ans))
print(*ans)
