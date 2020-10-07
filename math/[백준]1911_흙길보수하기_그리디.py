import sys
import math
N,L=map(int,input().split())
pool=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    pool.append([a,b])
pool.sort()

ans=0
last=0
for i in range(N):
    a,b=pool[i]
    start=max(a,last)
    if start>=b:
        last=start
        continue

    cnt=math.ceil((b-start)/L)
    ans+=cnt
    last=start+cnt*L

print(ans)