from collections import deque
import sys

dR=[0,0,-1,1]
dC=[1,-1,0,0]
N,M=map(int,input().split())

L=[]
for i in range(N):
    L.append(list(input()))

def dist(sR,sC,fR,fC):
    q=deque([[sR,sC]])
    visited=[[0 for j in range(N)] for i in range(N)]
    while(q):
        r,c=q.popleft()
        if r==fR and c==fC:
            return visited[r][c]
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==0 and L[tempR][tempC]!="1":
                visited[tempR][tempC]=visited[r][c]+1
                q.append([tempR,tempC])
    return -1

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a

loc=[]
for i in range(N):
    for j in range(N):
        if L[i][j]=="S" or L[i][j]=="K":
            loc.append([i,j])

parent=[i for i in range(M+1)]
edge=[]
for i in range(M+1):
    for j in range(i+1,M+1):
       d=dist(loc[i][0],loc[i][1],loc[j][0],loc[j][1])
       if d==-1:
           print(-1)
           sys.exit(1)
       edge.append([d,i,j])
edge.sort()
size=len(edge)

ans=0
cnt=0
for i in range(size):
    cost,a,b=edge[i]
    if find(a)!=find(b):
        union(a,b)
        cnt+=1
        ans+=cost
    if cnt==M:
        break
print(ans)
