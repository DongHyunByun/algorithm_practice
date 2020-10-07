import sys
import math

def treeInit(node,start,end):
    if start==end:
        tree[node]=L[start-1]
        return tree[node]

    mid=(start+end)//2

    tree[node]=treeInit(2*node,start,mid)+treeInit(2*node+1,mid+1,end)
    return tree[node]

def update(node,start,end,index,diff):
    if not (start<=index<=end):
        return

    tree[node]+=diff

    if (start!=end):
        mid=(start+end)//2
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

def mySum(node,start,end,left,right):
    if left>end or right<start:
        return 0
    elif left<=start and end <=right:
        return tree[node]
    mid=(start+end)//2

    return mySum(node*2,start,mid,left,right)+mySum(node*2+1,mid+1,end,left,right)




N,M,K=map(int,input().split())

# 입력값 받
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline().strip()))

# 트리 초기화
treeSize=2**(math.ceil(math.log(N,2))+1)
tree=[0 for i in range(treeSize)]
treeInit(1,1,N)


for i in range(M+K):
    #print("이전",tree)
    a,b,c=map(int,input().split())
    if a==1:
        v=c-L[b-1]
        L[b-1]=c
        update(1,1,N,b,v)
    else:
        print(mySum(1,1,N,b,c))
    #print("이후",tree)
