def solution(startNode,nowNode,visitedV,totalLen):
    global minCy

    if nowNode==startNode and totalLen!=0:
        if minCy>totalLen:
            minCy=totalLen
            return

    for i in graph:
        if (i[0]==nowNode) and (i not in visitedV) and (totalLen+i[2]<minCy) :
            solution(startNode,i[1],visitedV+[i],totalLen+i[2])


for t in range(int(input())):
    N,M=map(int,input().split())
    graph=[]
    for i in range(M):
        graph.append(list(map(int,input().split())))
    node=[i for i in range(1,N+1)]

    minCy=999999999999999
    #노드별로 사이클 확인
    for n in node:
        solution(n,n,[],0)

    print(f"#{t+1} {minCy}")
        