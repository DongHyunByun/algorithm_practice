from collections import deque

def manhaten(a,b,c,d):
    return abs(a-c)+abs(b-d)


T=int(input())
for t in range(T):
    ans = "sad"
    N=int(input())
    homeX,homeY=map(int,input().split())
    convL = []
    visited=[0 for i in range(N)]
    for i in range(N):
        convL.append(list(map(int,input().split())))

    toX,toY=map(int,input().split())
    q=deque([[homeX,homeY]])
    while(q):
        temp=q.popleft()
        r=temp[0]
        c=temp[1]
        # 목적지까지 가능하면 끝남
        if manhaten(r,c,toX,toY)<=1000:
            ans="happy"
            break
        for i in range(N):
            if visited[i]==0 and manhaten(convL[i][0],convL[i][1],r,c)<=1000:
                q.append([convL[i][0],convL[i][1]])
                visited[i]=1
    print(ans)