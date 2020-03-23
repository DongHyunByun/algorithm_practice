import sys
N,M=map(int,input().split())
edge=[]
for i in range(M):
    a,b,c=map(int, sys.stdin.readline().rstrip().split())
    edge.append([c,a,b])
edge.sort()
parent=[i for i in range(N+1)]

#루트노드 찾기
def find(a):
    if a==parent[a]:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a

ans=0
cnt=0
for i in range(M):
    c,a,b=edge[i]
    if not find(a)==find(b):
        ans+=c
        union(a,b)
        cnt+=1
    if cnt==N-2:
        break
print(ans)
