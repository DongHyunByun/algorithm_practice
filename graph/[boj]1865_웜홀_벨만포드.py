maxNum=987653210

def bellman():
    nodeDist=[maxNum for i in range(N+1)]
    nodeDist[1]=0
    isUpdate=False
    #총 V-1번 수행
    for i in range(N):
        isUpdate=False
        for n1,n2,cost in edge:
            #모두 연결아니면 아래생략으로 답찾기 가능
            if nodeDist[n1]==maxNum:
                continue
            nowDist=nodeDist[n1]+cost
            if nowDist<nodeDist[n2]:
                isUpdate=True
                nodeDist[n2]=nowDist
    return isUpdate


T=int(input())
for t in range(T):
    N,M,W=map(int,input().split())
    edge=[]
    for m in range(M):
        S,E,T=map(int,input().split())
        edge.append([S,E,T])
        edge.append([E,S,T])
    for w in range(W):
        S,E,T=map(int,input().split())
        edge.append([S,E,-T])
    if bellman():
        print("YES")
    else:
        print("NO")