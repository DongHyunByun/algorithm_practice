def solution(scoville, K):
    ans=0
    scoville.sort()
    while ( scoville[0] <K):
        if len(scoville)==1:
            return -1
        scoville=remove(scoville)
        ans+=1
    return ans

def remove(scoville):
    temp=scoville[0]+scoville[1]*2
    del scoville[0]
    del scoville[0]
    for i in range(len(scoville)):
        if (scoville[i]>=temp):
            scoville.insert(i,temp)
            print( scoville )
            return scoville

while(1) :
    scoville=list(map(int,input().split()))
    print(solution(scoville,7))