N,M=map(int,input().split())

want=[]
for i in range(N):
    temp=list(map(int,input().split()))
    want.append(temp[1:])

def solve(c):
    global ans

    if visited[c]==1:
        return 0
    visited[c]=1
    for w in want[c]:
        if room[w]==-1 or solve(room[w]):
            room[w]=c
            return 1 #갈 수 있는 방이 있으

    return 0 # 갈 수 있는 방이 없으면

ans=0
room=[-1 for i in range(M+1)]
for i in range(N):
    visited=[0 for i in range(N)]
    if solve(i):
        ans+=1


print(ans)