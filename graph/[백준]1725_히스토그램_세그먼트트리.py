import math
import sys

sys.setrecursionlimit(10**6)

def init(node,start,end):
    if start==end:
        tree[node]=L[start],start
        return tree[node]

    mid=(start+end)//2
    tree[node]=min(init(node*2,start,mid),init(node*2+1,mid+1,end))
    return tree[node]

# 리턴 : [최솟값, 인덱스]
def find(node,start,end,left,right):
    if left<=start and end<=right:
        return tree[node]
    elif end<left or right<start:
        return 1000000001,0
    else:
        mid=(start+end)//2
        return min(find(node*2,start,mid,left,right),find(node*2+1,mid+1,end,left,right))

def dfs(s,e):
    if e<s:
        return 0
    minH,indx=find(1,1,N,s,e)
    now=(e-s+1)*minH
    return max(now,dfs(s,indx-1),dfs(indx+1,e))




N=int(input())
L=[0]
for i in range(N):
    L.append(int(sys.stdin.readline().rstrip()))

size=2**(math.ceil(math.log(N,2))+1)
tree=[0 for i in range(size)]
init(1,1,N)
print(dfs(1,N))
