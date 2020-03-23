from collections import deque
F,S,G,U,D=map(int,input().split())
L=[-1 for i in range(F+1)]
q=deque([S])
L[S]=0
ans="use the stairs"
while(q):
    temp=q.popleft()
    if temp==G:
        ans=L[temp]
        break

    up=temp+U
    if up<=F and L[up]==-1:
        L[up]=L[temp]+1
        q.append(up)
    down=temp-D
    if down>=1 and L[down]==-1:
        L[down]=L[temp]+1
        q.append(down)
print(ans)