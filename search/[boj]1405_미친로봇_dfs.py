M,E,W,S,N=map(int,input().split())
probL=[E/100,W/100,N/100,S/100]
dR=[0,0,-1,1]
dC=[1,-1,0,0]

visited=[[0 for j in range(100)] for i in range(100)]

# n번째에 r,c에 갈수있는 확률은 prob
# 안단순할 확률을 구한다
def dfs(n,r,c,prob):
    global ans
    if n==M:
        return
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        tempProb=prob*probL[k]
        # 또방문(안단순)
        if visited[tempR][tempC]==1:
            ans+=tempProb
        else:
            visited[tempR][tempC]=1
            dfs(n+1,tempR,tempC,tempProb)
            visited[tempR][tempC]=0

ans=0
visited[50][50]=1
dfs(0,50,50,1)
print(1-ans)