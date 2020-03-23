from itertools import combinations
T=int(input())

def costCal(x1,y1,x2,y2):
    return (abs(x1-x2)**2+abs(y1-y2)**2)*E

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
    #입력
    N=int(input())
    xL = list(map(int,input().split()))
    yL = list(map(int, input().split()))
    E=float(input())

    #환경부담금 계산
    com = list(combinations([i for i in range(N)], 2))
    edge=[]
    for node1,node2 in com:
        cost=costCal(xL[node1],yL[node1],xL[node2],yL[node2])
        edge.append([cost,node1,node2])
    edge.sort()

    #크루스칼
    parent=[i for i in range(N)]
    size=len(edge)
    uniNum=0
    uniCost=0
    for i in range(size):
        c,a,b=edge[i]
        if find(a)!=find(b):
            union(a,b)
            uniNum+=1
            uniCost+=c
            if uniNum==N-1:
                break
    print("#%d %d"%(t+1,round(uniCost)))