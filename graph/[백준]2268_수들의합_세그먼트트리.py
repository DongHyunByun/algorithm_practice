import math
import sys



def init(node,start,end):
    if start==end:
        tree[node]=L[start]
        return tree[node]

    mid=(start+end)//2
    tree[node]=init(node*2,start,mid)+init(node*2+1,mid+1,end)
    return tree[node]

def mySum(node,start,end,left,right):
    if left<=start and end<=right:
        return tree[node]
    elif end<left or right<start:
        return 0
    else:
        mid=(start+end)//2
        return mySum(node*2,start,mid,left,right)+mySum(node*2+1,mid+1,end,left,right)

def change(node,start,end,index,s):
    if not start<=index<=end:
        return

    tree[node]+=s

    if start==end:
        return
    else:
        mid=(start+end)//2
        change(node*2,start,mid,index,s)
        change(node*2+1,mid+1,end,index,s)




N,M=map(int,input().split())
L=[0 for i in range(N+1)]
size=2**(math.ceil(math.log(N,2))+1)
tree=[0 for i in range(size)]
init(1,1,N)

for i in range(M):
    k,a,b=map(int,sys.stdin.readline().rstrip().split())
    # 합구하기
    if k==0:
        if a>b:
            a,b=b,a
        print(mySum(1,1,N,a,b))
    # 수정하기
    else:
        s=b-L[a]
        L[a]=b
        change(1,1,N,a,s)

