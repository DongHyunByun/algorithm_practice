import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    ans=0
    while(scoville[0]<K):
        if len(scoville)==1:
            return -1
        
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+2*b)
        ans+=1
    return ans