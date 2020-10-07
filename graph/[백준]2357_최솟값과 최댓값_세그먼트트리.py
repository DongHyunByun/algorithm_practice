import sys
import math

maxNum=math.inf
minNum=-math.inf

def init(node,start,end):
    if start==end:
        tree[node]=[L[start-1],L[start-1]]
        return tree[node]

    mid=(start+end)//2

    left=init(node*2,start,mid)
    right=init(node*2+1,mid+1,end)
    tree[node][0]=min(left[0],right[0])
    tree[node][1]=max(left[1],right[1])
    return tree[node]

def find(node,start,end,left,right):
    if left<=start and end<=right:
        return tree[node]
    elif right<start or end<left:
        return [maxNum,minNum]
    else:
        mid=(start+end)//2
        leftL=find(node*2,start,mid,left,right)
        rightL=find(node*2+1,mid+1,end,left,right)
        return [min(leftL[0],rightL[0]),max(leftL[1],rightL[1])]

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline().rstrip()))

# 트리 초기화
size=2**(math.ceil(math.log(N,2))+1)
tree=[[0,0] for _ in range(size)]
init(1,1,N)


for i in range(M):
    a,b=map(int,input().split())
    print(*find(1,1,N,a,b))


