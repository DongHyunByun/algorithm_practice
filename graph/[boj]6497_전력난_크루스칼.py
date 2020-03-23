import sys

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

while(1):
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    edge=[]
    total=0
    for i in range(n):
        a,b,c=map(int,sys.stdin.readline().rstrip().split())
        total+=c
        edge.append([c,a,b])
    edge.sort()
    parent=[i for i in range(m+1)]

    cnt=0
    cost=0
    for i in range(n):
        c,a,b=edge[i]
        if find(a)!=find(b):
            cost+=c
            cnt+=1
            union(a,b)
            if cnt==m-1:
                break

    print(total-cost)

