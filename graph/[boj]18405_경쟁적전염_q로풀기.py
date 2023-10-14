from collections import deque

dR= [0,0,-1,1]
dC= [1,-1,0,0]

N,K=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
S,X,Y=map(int,input().split())
X-=1
Y-=1

virus_dict = {i:[] for i in range(1,K+1)}
for i in range(N):
    for j in range(N):
        if L[i][j]!=0:
            virus_dict[L[i][j]].append([i,j])

q=deque([])
for virus in range(1,K+1):
    for r,c in virus_dict[virus]:
        q.append([r,c,0])

while(q):
    r,c,t = q.popleft()
    virus = L[r][c]

    for k in range(4):
        next_r = r+dR[k]
        next_c = c+dC[k]
        if 0<=next_r<N and 0<=next_c<N and L[next_r][next_c]==0:
            if t!=S:
                L[next_r][next_c] = virus
                q.append([next_r,next_c,t+1])

# for i in L:
#     print(i)

print(L[X][Y])