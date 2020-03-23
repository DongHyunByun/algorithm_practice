from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]

N=int(input())
L=[]
for i in range(N):
    L.append(list(input()))
def search():
    colorNum=0
    visited=[[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                colorNum+=1
                q=deque([[i,j]])
                visited[i][j]=colorNum
                nowColor=L[i][j]
                while(q):
                    temp=q.popleft()
                    r=temp[0]
                    c=temp[1]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==0 and nowColor==L[tempR][tempC]:
                            visited[tempR][tempC]=colorNum
                            q.append([tempR,tempC])
    return colorNum

a=search()
#R,G를 똑같이
for i in range(N):
    for j in range(N):
        if not L[i][j]=="B":
            L[i][j]="R"
b=search()
print(a,b)
