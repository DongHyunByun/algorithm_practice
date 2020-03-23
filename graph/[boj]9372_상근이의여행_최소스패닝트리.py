import sys

T=int(input())
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

for t in range(T):
    N,M=map(int,sys.stdin.readline().rstrip().split())
    edge=[]
    for i in range(M):
        a,b=map(int,sys.stdin.readline().rstrip().split())
        edge.append([a,b])
    parent=[i for i in range(N+1)]
    cnt=0
    for a,b in edge:
        if find(a)!=find(b):
            cnt+=1
            union(a,b)
            if cnt==N-1:
                break
    print(cnt)