import heapq
INF=976543210

N,D=map(int,input().split())

graph={}

point=set({0,D})
for i in range(N):
    a,b,w=map(int,input().split())
    point.add(a)
    if b<D:
        point.add(b)

    if a in graph:
        graph[a].append([b,w])
    else:
        graph[a]=[[b,w]]

point=sorted(point)
point_size=len(point)
for i in range(point_size-1):
    a=point[i]
    b=point[i+1]
    w=b-a
    if a in graph:
        graph[a].append([b,w])
    else:
        graph[a]=[[b,w]]

dist=[INF for i in range(D+1)]
pq=[[0,0]]
dist[0]=0

while pq:
    nowDist,nowNode = heapq.heappop(pq)
    if dist[nowNode] < nowDist:
        continue

    if nowNode==D:
        print(nowDist)
        break

    for toNode,addDist in graph[nowNode]:
        addedDist = addDist + nowDist
        if toNode<=D and addedDist < dist[toNode]:
            dist[toNode]=addedDist
            heapq.heappush(pq,[addedDist,toNode])


