N,M=map(int,input().split())

INF=9876543210
dist = [[INF for j in range(N)] for i in range(N)]
dist_r = [[INF for j in range(N)] for i in range(N)]
min_count = N//2+1

for i in range(N):
    dist[i][i]=0
    dist_r[i][i]=0

for i in range(M):
    a,b=map(int,input().split())
    dist[a-1][b-1]=1
    dist_r[b-1][a-1]=1

def floid(dist):
    for k in range(N):
        for i in range(N):
            if dist[i][k]==INF:
                continue
            for j in range(N):
                if dist[k][j]==INF:
                    continue
                if dist[i][k]+dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]

floid(dist)
floid(dist_r)

# for i in dist:
#     print(i)
# print()
# for i in dist_r:
#     print(i)

ans=0
for i in range(N):
    cnt=0
    cnt_r=0
    for j in range(N):
        if dist[i][j] not in (0,INF):
            cnt+=1
        if dist_r[i][j] not in (0,INF):
            cnt_r+=1

    if min_count<=cnt or min_count<=cnt_r:
        ans+=1
print(ans)