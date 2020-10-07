N,M=map(int,input().split())

room=[0 for i in range(N+1)]
want=[[] for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    want[a].append(b)

def solve(i):
    if visited[i]==1:
        return 0
    visited[i]=1
    for w in want[i]:
        if room[w]==0 or solve(room[w]):
            room[w]=i
            return 1
    return 0


ans=0
for i in range(1,N+1):
    visited=[0 for i in range(N+1)]
    if solve(i):
        ans+=1

print(ans)