N=int(input())
graph={}
INF=9876543210

def inorder(n,r):
    global col
    left,right=graph[n]

    if left!=-1:
        inorder(left,r+1)

    if col<L[r][0]:
        L[r][0]=col
    if col>L[r][1]:
        L[r][1]=col
    col+=1

    if right!=-1:
        inorder(right,r+1)

# 입력
parent=[0 for i in range(N+1)]
for _ in range(N):
    node,left,right=map(int,input().split())
    graph[node]=left,right
    if left!=-1:
        parent[left]=1
    if right!=-1:
        parent[right]=1


# 루트노드찾기
for i in range(1,N+1):
    if parent[i]==0:
        root=i
        break

# 중위순회
L=[[INF,-INF] for i in range(N+1)] # L[i][0] : i레밸의 가장왼쪽, L[i][1] : i레벨의 가장 오른쪽
col=1
inorder(root,1)
#print(L)

# 최대넓이와 그때레밸
lv=0
maxW=0
for i in range(1,N+1):
    temp=L[i][1]-L[i][0]+1
    if temp>maxW:
        lv=i
        maxW=temp
print(lv,maxW)
