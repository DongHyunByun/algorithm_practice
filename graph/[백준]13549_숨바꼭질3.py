import heapq
N,K=map(int,input().split())

INF=9876543210
maxNum=100001
dist=[INF for i in range(maxNum)]
pq=[[0,N]]
dist[N]=0

while(pq):
    time,loc=heapq.heappop(pq)
    #print(time,loc)
    if dist[loc]<time:
        continue
    # 동생이 있는위치면?
    if K==loc:
        print(dist[K])
        break

    #순간이동
    newLoc=loc*2
    while(newLoc!=0):
        if maxNum<=newLoc:
            break
        if time<dist[newLoc]:
            heapq.heappush(pq,[time,newLoc])
            dist[newLoc]=time
        newLoc*=2
    #한칸뒤로
    if loc!=0 and time+1<dist[loc-1]:
        heapq.heappush(pq,[time+1,loc-1])
        dist[loc-1]=time+1
    #한칸앞으로
    if loc!=100000 and time+1<dist[loc+1]:
        heapq.heappush(pq,[time+1,loc+1])
        dist[loc+1]=time+1











