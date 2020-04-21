import sys

INF = 9876543210
V, E = map(int, input().split())
L=[[0 for j in range(V)] for i in range(V)]

for i in range(V):
    for j in range(V):
        L[i][j]=INF

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    L[a-1][b-1]=c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if L[i][j]>L[i][k]+L[k][j]:
                L[i][j]=L[i][k]+L[k][j]

ans=INF
for i in range(V):
    if L[i][i]<ans:
        ans=L[i][i]

if ans==INF:
    print(-1)
else:
    print(ans)