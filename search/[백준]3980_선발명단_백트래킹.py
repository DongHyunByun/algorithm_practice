T=int(input())

def dfs(player,visited):
    global ans
    if player==11:
        nowSum=sum(visited)
        if ans<nowSum:
            ans=nowSum
        return

    isFind=False
    for pos in range(11):
        if visited[pos]==0 and L[player][pos]!=0:
            isFind=True
            visited[pos]=L[player][pos]
            dfs(player+1,visited)
            visited[pos]=0

    if isFind==False:
        return


for t in range(T):
    ans=0
    L=[]
    for i in range(11):
        L.append(list(map(int,input().split())))
    visited=[0 for i in range(11)]

    dfs(0,visited)
    print(ans)
