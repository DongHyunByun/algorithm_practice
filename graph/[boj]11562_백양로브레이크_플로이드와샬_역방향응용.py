import sys
n,m = map(int,input().split())

INF=9876543210
dist = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    dist[i][i]=0

for i in range(m):
    u,v,b = map(int,sys.stdin.readline().rstrip().split())
    dist[u][v] = 0
    if b==0:
        dist[v][u]=1
    else:
        dist[v][u]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        if dist[i][k]==INF:
            continue
        for j in range(1,n+1):
            if dist[k][j]==INF:
                continue
            if dist[i][k]+dist[k][j]<dist[i][j]:
                dist[i][j]=dist[i][k]+dist[k][j]

k = int(input())
for i in range(k):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(dist[a][b])
