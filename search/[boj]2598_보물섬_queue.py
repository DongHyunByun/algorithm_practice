from collections import deque

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(input()))
dR=[0,0,-1,1]
dC=[1,-1,0,0]

def main():
    ans=0
    for i in range(N):
        for j in range(M):
            if L[i][j]=="L":
                #print(i,j,"i와 j")
                visited=[[-1 for j in range(M)] for i in range(N)]
                q=deque([[i,j]])
                visited[i][j]=0
                while(q):
                    temp=q.popleft()
                    #print(temp)
                    r=temp[0]
                    c=temp[1]
                    lastNum=visited[r][c]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]=="L" and visited[tempR][tempC]==-1:
                            visited[tempR][tempC]=visited[r][c]+1
                            q.append([tempR,tempC])
                if lastNum>ans:
                    ans=lastNum
    print(ans)

main()