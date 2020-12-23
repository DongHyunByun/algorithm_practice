from collections import deque

maxNum=100000
N,K=map(int,input().split())

visited=[-1 for i in range(maxNum+1)]
q=deque([(N,0)])
case=0

T=maxNum+1
while(q):
    loc,t=q.popleft()
    if t>T:
        break

    if visited[loc]==-1:
        visited[loc]=t

    if loc==K:
        T=t
        case+=1
        continue

    #걷기
    if loc+1<=maxNum and visited[loc+1]==-1:
            q.append((loc+1,t+1))
    if loc-1>=0 and visited[loc-1]==-1:
            q.append((loc-1,t+1))
    #순간이동
    if 2*loc<=maxNum and visited[2*loc]==-1:
            q.append((2*loc,t+1))

print(T)
print(case)