 from collections import deque

N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

ansL=[[0 for j in range(N)] for i in range(N)]

# 점 하나씩 검사
for i in range(N):
    q=deque([])
    #첫 q넣기
    for j in range(N):
        if L[i][j]==1 :
            q.append(j)
            ansL[i][j]=1
    while(q):
        temp=q.popleft()
        for j in range(N):
            if L[temp][j]==1 and ansL[i][j]==0:
                q.append(j)
                ansL[i][j]=1

for i in range(N):
    for j in range(N):
        print(ansL[i][j],end=" ")
    print()