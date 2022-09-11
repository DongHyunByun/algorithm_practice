import heapq

def solution(n, paths, gates, summits):
    # graph 세팅
    graph={i:[] for i in range(1,n+1)}
    for a,b,dist in paths:
        graph[a].append((b,dist))
        graph[b].append((a,dist))

    INF=9876543210
    visited=[INF for i in range(n+1)]
    dij = []
    for start_node in gates:
        visited[start_node]=0
        dij.append((0,start_node))

    ans = []
    while(dij):
        d,node = heapq.heappop(dij)
        # print(node,d)
        # print(visited)
        if visited[node]<d:
            continue

        if node in summits:
            ans.append([visited[node],node])
            continue

        for to_node,add_dist in graph[node]:
            added_dist = max(visited[node],add_dist)
            if added_dist < visited[to_node]:
                visited[to_node] = added_dist
                heapq.heappush(dij,(visited[to_node],to_node))

    ans.sort()
    return [ans[0][1],ans[0][0]]