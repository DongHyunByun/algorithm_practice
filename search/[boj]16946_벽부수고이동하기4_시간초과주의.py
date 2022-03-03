from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]

N,M = map(int,input().split())

L=[]
for i in range(N):
    L.append(list(input()))

component_dict = {}
component_code = 0
visited=[[-1 for j in range(M)] for i in range(N)]


def bfs(sR,sC,component_code):
    cnt = 1
    q = deque([(sR,sC)])
    visited[sR][sC]=component_code

    while(q):
        r,c = q.popleft()
        for k in range(4):
            next_r=r+dR[k]
            next_c=c+dC[k]
            if 0<=next_r<N and 0<=next_c<M and visited[next_r][next_c]==-1 and L[next_r][next_c]=="0":
                cnt+=1
                q.append((next_r,next_c))
                visited[next_r][next_c]=component_code

    return cnt


for i in range(N):
    for j in range(M):
        if L[i][j]=="0" and visited[i][j]==-1:
            component_cnt = bfs(i,j,component_code)
            component_dict[component_code] = component_cnt
            component_code+=1

ans=[["0" for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        if L[i][j]=="1":
            # print(i,j)
            cnt=1
            code_map = set()
            for k in range(4):
                next_i = i+dR[k]
                next_j = j+dC[k]
                if 0<=next_i<N and 0<=next_j<M and visited[next_i][next_j]!=-1:
                    code_map.add(visited[next_i][next_j])
            for c in code_map:
                cnt+=component_dict[c]

            ans[i][j] = str(cnt%10)

for i in ans:
    print("".join(i))




