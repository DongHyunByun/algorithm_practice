from collections import deque
from itertools import combinations

N,K=input().split()
size=len(N)
#N=int(N)
K=int(K)
q=deque([[N,0]])
ans=-1
comb=list(combinations([i for i in range(size)],2))
visited=[[0 for j in range(1000001)] for i in range(K)]

while(q):
    num,time=q.popleft()
    #print(num,time)
    if time==K:
        if int(num)>ans:
            ans=int(num)
        continue
    #교환
    used=[]
    for a,b in comb:
        if num[b]=="0" and a==0:
            continue
        temp=list(num)
        temp[a],temp[b]=temp[b],temp[a]
        newN="".join(temp)
        intNewN=int(newN)
        if not visited[time-1][intNewN]:
            visited[time-1][intNewN]=1
            q.append([newN,time+1])
print(ans)
