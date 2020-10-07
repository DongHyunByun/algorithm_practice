import math
import sys

def initTree(node,start,end):
    if start==end:
        tree[node]=L[start-1]
        return tree[node]

    mid=(start+end)//2

    tree[node]=min(initTree(node*2,start,mid),initTree(node*2+1,mid+1,end))
    return tree[node]

def findMin(node,start,end,left,right):
    if left<=start and end<=right:
        return tree[node]
    elif right<start or end<left:
        return math.inf
    else:
        mid=(start+end)//2
        return min(findMin(node*2,start,mid,left,right),findMin(node*2+1,mid+1,end,left,right))

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline().rstrip()))

size=2**(math.ceil(math.log(N,2))+1)
tree=[0 for _ in range(size)]
initTree(1,1,N)

for i in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    print(findMin(1,1,N,a,b))