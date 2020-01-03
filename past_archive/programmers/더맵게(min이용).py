def solution(scoville, K):
    ans=0
    
    while(1):
        a=min(scoville)
        if (a>=K):
            return ans
        if len(scoville)==1 :
            return -1
        
        scoville.remove(a)
        b=min(scoville)
        scoville.remove(b)
        scoville.append(a+2*b)
        ans+=1
        
    return ans