from itertools import combinations

dR=[0,0,-1,1]
dC=[1,-1,0,0]
comb=list(combinations([i for i in range(25)],7))
L=[]
for i in range(5):
    L.append(input())


def cntY(loc):
    cnt=0
    for i in range(7):
        r=loc[i][0]
        c=loc[i][1]
        if L[r][c]=="Y":
            cnt+=1
    return cnt

def dfs(r,c):
    global cnt
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<5 and 0<=tempC<5 and temp[tempR][tempC]==1 and visited[tempR][tempC]==0:
            cnt+=1
            visited[tempR][tempC]=1
            dfs(tempR,tempC)



ans=0
for com in comb:
    loc=[]
    for i in range(7):
        r=com[i]//5
        c=com[i]%5
        loc.append([r,c])
    # 네명 이하면 붙어있는지 확인
    if cntY(loc)<4:
        cnt=1
        temp = [[0 for j in range(5)] for i in range(5)]
        visited = [[0 for j in range(5)] for i in range(5)]
        for r,c in loc:
            temp[r][c]=1
        visited[loc[0][0]][loc[0][1]]=1
        dfs(loc[0][0],loc[0][1])

        if cnt==7:
            ans+=1

print(ans)