from collections import deque
from itertools import permutations,product
from copy import deepcopy
L=[]

dR=(0,0,-1,1,0,0)
dC=(1,-1,0,0,0,0)
dH=(0,0,0,0,1,-1)

for i in range(5):
    layer=[]
    for j in range(5):
        temp=list(map(int,input().split()))
        layer.append(temp)
    L.append(layer)

def bfs(cube):
    if cube[0][0][0]==0:
        return 200

    visited=[[[-1 for k in range(5)] for j in range(5)] for i in range(5)]
    visited[0][0][0]=0
    q=deque([[0,0,0]])

    while(q):
        r,c,h=q.popleft()
        if r==4 and c==4 and h==4:
            return visited[r][c][h]
        for k in range(6):
            tempR=r+dR[k]
            tempC=c+dC[k]
            tempH=h+dH[k]
            if 0<=tempR<5 and 0<=tempC<5 and 0<=tempH<5 and visited[tempR][tempC][tempH]==-1 and cube[tempR][tempC][tempH]:
                visited[tempR][tempC][tempH]=visited[r][c][h]+1
                q.append([tempR,tempC,tempH])

    return 200

per=list(permutations([i for i in range(5)],5))

ans=200

for case in per:
    total=[]
    for i in case:
        total.append(L[i])

    for p in product([0,1,2,3], repeat=5):
        cube=[]
        for i,rotate in enumerate(p):
            temp=total[i]
            for _ in range(rotate):
                temp=list(map(list, zip(*temp[::-1])))
            cube.append(temp)

        dist=bfs(cube)
        if dist<ans:
            ans=dist
        if ans==12:
            break
    if ans==12:
        break


if ans==200:
    print(-1)
else:
    print(ans)



