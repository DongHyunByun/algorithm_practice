import sys
T=int(input())
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

for t in range(T):
    F=int(input())
    parent={}
    cntByRoot={}
    for _ in range(F):
        a,b=sys.stdin.readline().rstrip().split()
        if a in parent:
            isA=True
        else:
            isA=False
        if b in parent:
            isB=True
        else:
            isB=False

        if isA and isB:
            rootA=find(a)
            rootB=find(b)
            if rootA!=rootB:
                union(rootA,rootB)
                cntByRoot[rootA]+=cntByRoot[rootB]
            print(cntByRoot[rootA])
        elif isA and not isB:
            root=find(a)
            parent[b]=root
            cntByRoot[root]+=1
            print(cntByRoot[root])
        elif not isA and isB:
            root=find(b)
            parent[a]=root
            cntByRoot[root]+=1
            print(cntByRoot[root])
        else:
            parent[a]=a
            parent[b]=a
            cntByRoot[a]=2
            print(cntByRoot[a])



