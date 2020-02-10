import heapq
maxNum=9876543210

def main():
    #입력
    N,E=map(int,input().split())
    if E==0:
        print(-1)
        return
    graph={}
    for i in range(N):
        graph[i+1]=[]
    for i in range(E):
        a,b,c=map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    node1,node2=map(int,input().split())


    ansDist=[0,0,0,0,0]
    #(시작점에서 node1, node2까지)와 (마지막점에서 node1,node2)까지
    find = [[1, node1, node2], [N, node1, node2]]
    for i in range(2):
        nodeDist=[maxNum for i in range(N+1)]
        dij=[[0,find[i][0]]]
        nodeDist[find[i][0]]=0
        while(dij):
            temp=heapq.heappop(dij)
            nowCost=temp[0]
            nowNode=temp[1]
            if nodeDist[nowNode]<nowCost:
                continue

            if nowNode == find[0][1]:
                ansDist[2*i]=nowCost
            elif nowNode == find[0][2]:
                ansDist[2*i+1]=nowCost
            if ansDist[2*i]!=0 and ansDist[2*i+1]!=0:
                break
            for toNode,toCost in graph[nowNode]:
                w=nodeDist[nowNode]+toCost
                if nodeDist[toNode]>w:
                    nodeDist[toNode]=w
                    heapq.heappush(dij,[w,toNode])

    #node1과 node2사이 거리
    nodeDist = [maxNum for i in range(N + 1)]
    dij = [[0, node1]]
    nodeDist[node1] = 0
    while (dij):
        temp = heapq.heappop(dij)
        nowCost = temp[0]
        nowNode = temp[1]
        if nodeDist[nowNode] < nowCost:
            continue
        if nowNode==node2:
            ansDist[4]=nowCost
            break
        for toNode, toCost in graph[nowNode]:
            w = nodeDist[nowNode] + toCost
            if nodeDist[toNode] > w:
                nodeDist[toNode] = w
                heapq.heappush(dij, [w, toNode])

    ans=min(ansDist[0]+ansDist[3]+ansDist[4],ansDist[1]+ansDist[2]+ansDist[4])
    if ans>maxNum:
        print(-1)
    else:
        print(ans)
main()