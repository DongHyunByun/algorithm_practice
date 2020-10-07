import heapq
INF=9876543210

dR=[0,0,-1,1]
dC=[1,-1,0,0]

N=int(input())
L=[]
for i in range(N):
    temp=list(input())
    L.append(temp)

dist=[[INF for j in range(N)] for i in range(N)]
dist[0][0]=0
pq=[[0,0,0]]

while(pq):
    cost,r,c=heapq.heappop(pq)
    if dist[r][c]<cost:
        continue
    if r==N-1 and c==N-1:
        break
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<N and 0<=tempC<N:
            #하얀색?
            if L[tempR][tempC]=="1":
                if cost<dist[tempR][tempC]:
                    dist[tempR][tempC]=cost
                    heapq.heappush(pq,[cost,tempR,tempC])
            #검은색?
            else:
                if cost+1<dist[tempR][tempC]:
                    dist[tempR][tempC]=cost+1
                    heapq.heappush(pq,[cost+1,tempR,tempC])

print(dist[N-1][N-1])

