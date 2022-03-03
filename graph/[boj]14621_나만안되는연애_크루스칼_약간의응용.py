import sys

N,M=map(int,input().split())

col_gender = list(input().split())
parent = [i for i in range(N)]
edges = []

for i in range(M):
    a,b,cost = map(int,sys.stdin.readline().rstrip().split())
    edges.append((cost,a-1,b-1))

def is_cycle(node1,node2):
    def find(node):
        '''
        node의 루트노드를 확인한다
        '''
        if parent[node]==node:
            return node
        else:
            parent[node]=find(parent[node])
            return parent[node]

    def union(node1,node2):
        '''
        node1과 node2가 연결됨을 표현한다
        '''
        root1 = find(node1)
        root2 = find(node2)
        if root1!=root2:
            parent[root1] = root2

    if find(node1)==find(node2): # root노드가 같으면 연결되어있음
        return True
    else:
        union(node1,node2)
        return False

edges.sort()
cnt=0
ans=0
for edge in edges:
    cost,a,b = edge
    # print(cost,a,b)
    if (col_gender[a]!=col_gender[b]) and (not is_cycle(a,b)):
        cnt+=1
        ans+=cost
    if cnt==N-1:
        break

if cnt==N-1:
    print(ans)
else:
    print(-1)