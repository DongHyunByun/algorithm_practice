import sys

dR=[0,0,-1,1]
dC=[1,-1,0,0]

R,C=map(int,input().split())
L=[]
for i in range(R):
    L.append(list(input()))
visited=[0 for i in range(26)]
visited[ord(L[0][0])-65]=1
ans=0
def dfs(i,j,cnt):
    global ans
    for k in range(4):
        tempR=i+dR[k]
        tempC=j+dC[k]
        if 0<=tempR<R and 0<=tempC<C:
            #알파뱃 중복되면 종료
            num=ord(L[tempR][tempC])-65
            if visited[num]:
                if ans<cnt:
                    ans=cnt
                continue
            else:
                visited[num]=1
                if cnt==25:
                    print(26)
                    sys.exit()
                else:
                    dfs(tempR,tempC,cnt+1)
                visited[num]=0

dfs(0,0,1)
print(ans)