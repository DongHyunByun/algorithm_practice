from collections import deque

N,K=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
S,X,Y=map(int,input().split())
X-=1
Y-=1

def find_virus(L,v):
    start_list = []
    for i in range(N):
        for j in range(N):
            if L[i][j]==v:
                start_list.append((i,j))
    return start_list

def spread_virus(L,start_r,start_c):
    dR=[0,0,-1,1]
    dC=[1,-1,0,0]

    virus = L[start_r][start_c]
    visited_list[start_r][start_c]=1
    q = deque([[start_r,start_c]])

    next_start_list = []

    while(q):
        r,c = q.popleft()
        for k in range(4):
            next_r = r+dR[k]
            next_c = c+dC[k]

            if 0<=next_r<N and 0<=next_c<N and visited_list[next_r][next_c]==-1:
                if L[next_r][next_c]==0:
                    visited_list[next_r][next_c] = 1
                    L[next_r][next_c]=virus
                    next_start_list.append([next_r,next_c])
                elif L[next_r][next_c]==virus:
                    visited_list[next_r][next_c] = 1
                    q.append([next_r,next_c])

    return L,next_start_list

start_dict = {k:[] for k in range(1,K+1)}
for i in range(N):
    for j in range(N):
        if L[i][j]:
            start_dict[L[i][j]].append([i,j])

visited_list = [[-1 for j in range(N)] for i in range(N)]
for t in range(1,S+1):
    for virus in range(1,K+1):
        # print(virus,"바이러스")
        start_list = start_dict[virus]
        next_start_list = []
        for start_r,start_c in start_list:
            # print(start_r,start_c,virus,"확장!!")
            L,now_start_list = spread_virus(L,start_r,start_c)
            next_start_list.extend(now_start_list)
        start_dict[virus] = next_start_list
    # print(t,"번째 후")
    # for i in L:
    #     print(i)
    # print("start_Dict",start_dict)

print(L[X][Y])