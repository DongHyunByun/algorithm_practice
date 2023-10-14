from itertools import combinations
from copy import deepcopy
from collections import deque

N,M = map(int,input().split())
L = []
for i in range(N):
    L.append(list(map(int,input().split())))

virus_space = []
for i in range(N):
    for j in range(N):
        if L[i][j]==2:
            virus_space.append([i,j])

origin_L = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if L[i][j]==1:
            origin_L[i][j] = "-"
        else:
            origin_L[i][j] = -1

def get_min_time(virus_loc):
    max_time = 0

    dr=[0,0,-1,1]
    dc=[1,-1,0,0]

    q = deque([])
    # visited = [[-1 for j in range(N)] for i in range(N)]

    now_L=deepcopy(origin_L)
    for r,c in virus_loc:
        q.append([r,c])
        # visited[r][c]=1
        now_L[r][c]=0

    while(q):
        r,c =q.popleft()
        t = now_L[r][c]
        for k in range(4):
            next_r = r+dr[k]
            next_c = c+dc[k]
            if 0<=next_r<N and 0<=next_c<N and now_L[next_r][next_c]==-1:
                now_L[next_r][next_c]=t+1
                q.append([next_r,next_c])
                max_time = now_L[next_r][next_c]

    # print(virus_loc,"일떄!")
    # for i in now_L:
    #     print(i)

    for i in range(N):
        for j in range(N):
            if now_L[i][j]==-1:
                return -1
    return max_time





virus_combi_list = list(combinations(virus_space,M))

min_spread_time = 9876543210
is_can=False
for virus_loc in virus_combi_list:
    spread_time = get_min_time(virus_loc)
    # print(spread_time)
    if spread_time!=-1:
        is_can = True
        min_spread_time=min(min_spread_time,spread_time)

if is_can:
    print(min_spread_time)
else:
    print(-1)

