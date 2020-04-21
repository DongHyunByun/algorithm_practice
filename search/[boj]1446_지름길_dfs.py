N,D=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
L.sort()
def dfs(indx,loc,move):
    global ans
    if move>=ans or loc>D:
        return
    if loc==D:
        if move<ans:
            ans=move
        return
    if indx==N:
        if move+(D-loc)<ans:
            ans=move+(D-loc)
        return

    # indx번째 지름길 탈 수 있을 때
    if L[indx][0]>=loc:
        # 타는경우
        dfs(indx+1,L[indx][1],move+L[indx][2]+(L[indx][0]-loc))
        # 안타는경우
        dfs(indx+1,loc,move)
    # 탈 수 없는 경우
    else:
        dfs(indx+1,loc,move)

ans=D
dfs(0,0,0)
print(ans)