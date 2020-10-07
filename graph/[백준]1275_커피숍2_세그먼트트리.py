import math
import sys

def init(node,start,end):
    if start==end:
        tree[node]=L[start-1]
        return tree[node]

    mid=(start+end)//2
    tree[node]=init(node*2,start,mid)+init(node*2+1,mid+1,end)
    return tree[node]

def update(node,start,end,index,diff):
    if not start<=index<=end:
        return

    tree[node]+=diff

    if start!=end:
        mid=(start+end)//2
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

def treeSum(node,start,end,left,right):
    if left<=start and end<=right:
        return tree[node]
    elif right<start or end<left:
        return 0
    else:
        mid=(start+end)//2
        return treeSum(node*2,start,mid,left,right)+treeSum(node*2+1,mid+1,end,left,right)

N,Q=map(int,sys.stdin.readline().rstrip().split())
L=list(map(int,sys.stdin.readline().rstrip().split()))

size=2**(math.ceil(math.log(N,2))+1)
tree=[0 for i in range(size)]
init(1,1,N)

for i in range(Q):
    x,y,a,b=map(int,sys.stdin.readline().rstrip().split())
    if x>y:
        print(treeSum(1,1,N,y,x))
    else:
        print(treeSum(1,1,N,x,y))
    v=b-L[a-1]
    L[a-1]=b
    update(1,1,N,a,v)