N=int(input())
M=int(input())
INF=9876543210
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
order=list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if i==j:
            L[i][j]=0
        elif L[i][j]==0:
            L[i][j]=INF

#floid
for k in range(N):
    for i in range(N):
        for j in range(N):
            if L[i][j]>L[i][k]+L[k][j]:
                L[i][j]=L[i][k]+L[k][j]

ans="YES"
for i in range(M-1):
    fromC=order[i]-1
    toC=order[i+1]-1
    if L[fromC][toC]==INF:
        ans="NO"
        break
print(ans)

