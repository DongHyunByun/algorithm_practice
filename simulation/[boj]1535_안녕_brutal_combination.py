from itertools import combinations
N=int(input())
lost=list(map(int,input().split()))
get=list(map(int,input().split()))

ans=0
#i개를 선택할때
for i in range(1,N+1):
    comb=list(combinations([j for j in range(N)],i))
    for getL in comb:
        happy=0
        hp=0
        #기쁨계산
        for human in getL:
            hp+=lost[human]
            if hp>=100:
                break
            else:
                happy+=get[human]
        if hp<100 and happy>ans:
            ans=happy
print(ans)