from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]

n,m=map(int,input().split())
L=[]
for i in range(n):
    L.append(list(map(int,input().split())))

visited=[[0 for j in range(m)] for i in range(n)]

cnt=0
maxBroad=0
for i in range(n):
    for j in range(m):
        if L[i][j]==1 and visited[i][j]==0:
            q=deque([[i,j]])
            cnt+=1
            visited[i][j]=cnt
            broad=1
            while(q):
                r,c=q.popleft()
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<n and 0<=tempC<m and visited[tempR][tempC]==0 and L[tempR][tempC]==1:
                        broad+=1
                        q.append([tempR,tempC])
                        visited[tempR][tempC]=cnt
            if maxBroad<broad:
                maxBroad=broad

print(cnt)
print(maxBroad)
