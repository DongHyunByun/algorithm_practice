import heapq

# 입력
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
king = list(map(int, input().split()))
graph = {}
for i in range(N):
    graph[i + 1] = []
for i in range(M):
    U, V, L = map(int, input().split())
    graph[U].append([V, L])
    graph[V].append([U, L])

# 도로별 지나갈 수 없는 시간
stop = {}
t = 0
for i in range(G - 1):
    for nodes in graph[king[i]]:
        if nodes[0] == king[i + 1]:
            if king[i] < king[i + 1]:
                stop[(king[i], king[i + 1])] = [t, t + nodes[1] - 1]
            else:
                stop[(king[i + 1], king[i])] = [t, t + nodes[1] - 1]
            t += nodes[1]
            break

# 다익스트라 시작
inf = 9876543210
nodeDist = [inf for i in range(N + 1)]
dij = [[K, A]]
heapq.heapify(dij)
while(dij):
    temp = heapq.heappop(dij)
    time = temp[0]
    nowNode = temp[1]
    nodeDist[nowNode] = time
    if nowNode==B:
        ans=time-K
        break
    for toNode, addedTime in graph[nowNode]:
        tempTu = tuple(sorted([nowNode, toNode]))
        # 국왕이 길에 있을때
        if (tempTu in stop) and stop[tempTu][0] <= time <= stop[tempTu][1]:
            if nodeDist[toNode] > stop[tempTu][1] + 1 + addedTime:
                heapq.heappush(dij, [stop[tempTu][1] + 1 + addedTime, toNode])
        else :
            if nodeDist[toNode]>time+addedTime:
                heapq.heappush(dij, [time + addedTime, toNode])

print(ans)
