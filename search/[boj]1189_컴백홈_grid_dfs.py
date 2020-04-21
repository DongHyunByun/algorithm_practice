R,C,K=map(int,input().split())
L=[]
dR=[0,0,-1,1]
dC=[1,-1,0,0]
visited=[[0 for j in range(C)] for i in range(R)]

for i in range(R):
    L.append(list(input()))

def dfs(r,c,move):
    global ans
    if move>K:
        return
    if r==0 and c==C-1:
        if move==K:
            ans+=1
        return

    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<R and 0<=tempC<C and L[tempR][tempC]!="T" and visited[tempR][tempC]==0:
            visited[tempR][tempC]=1
            dfs(tempR,tempC,move+1)
            visited[tempR][tempC]=0

ans=0
visited[R-1][0]=1
dfs(R-1,0,1)
print(ans)