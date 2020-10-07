import math
import sys
mod=1000000007


def init(node,start,end):
    if start==end:
        tree[node]=L[start-1]
        return tree[node]

    mid=(start+end)//2

    tree[node]=(init(node*2,start,mid)*init(node*2+1,mid+1,end))%mod
    return tree[node]

def multi(node,start,end,left,right):
    if left<=start and end<=right:
        return tree[node]
    elif right<start or end<left:
        return 1
    else:
        mid=(start+end)//2
        return (multi(node*2,start,mid,left,right)*multi(node*2+1,mid+1,end,left,right))%mod

def update(node,start,end,index,val):
    if not start<=index<=end:
        return tree[node]
    elif start==end:
        tree[node]=val
        return tree[node]
    else:
        mid=(start+end)//2
        tree[node]=(update(node*2,start,mid,index,val)*update(node*2+1,mid+1,end,index,val))%mod
        return tree[node]

N,M,K=map(int,input().split())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline().strip()))

size=2**(math.ceil(math.log(N,2))+1)
tree=[1 for i in range(size)]
init(1,1,N)

for i in range(M+K):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    if a==1:
        update(1,1,N,b,c)
    else:
        print(multi(1,1,N,b,c))
