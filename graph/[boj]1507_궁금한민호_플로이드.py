import sys

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
edge=[[1 for j in range(N)] for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                edge[i][j]=-1
            elif i==k or k==j:
                continue
            elif L[i][j]==L[i][k]+L[k][j]:
                edge[i][j]=-1
            elif L[i][j]>L[i][k]+L[k][j]:
                print(-1)
                sys.exit()
ans=0
for i in range(N):
    for j in range(i,N):
        if edge[i][j]==1:
            ans+=L[i][j]

print(ans)