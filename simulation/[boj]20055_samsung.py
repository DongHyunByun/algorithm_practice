from collections import deque

N,K=map(int,input().split())

#벨트 [내구도, 로봇여부]
life=list(map(int,input().split()))
upperBelt=deque([[0,0] for i in range(N)])
lowerBelt=deque([[0,0] for i in range(N)])

for i in range(N):
    upperBelt[i][0]=life[i]
for i in range(N):
    lowerBelt[-1-i][0]=life[i+N]

#로봇의 위치
upperRobots=deque([])
countZero=0 #제로개수
ans=0

while(1):
    ans+=1

    # 전체회전
    lowerBelt.append([upperBelt.pop()[0],0])
    upperBelt.appendleft(lowerBelt.popleft())

    # 로봇이동
    for i in range(N-1,-1,-1):
        if upperBelt[i][1]==1:
            if i+1==N:
                upperBelt[N-1][1]=0
            elif upperBelt[i+1][0]>=1 and upperBelt[i+1][1]==0:
                upperBelt[i+1][1]=1
                upperBelt[i][1]=0

                upperBelt[i+1][0]-=1
                if upperBelt[i+1][0]==0:
                    countZero+=1

    # 로봇 올리기
    if upperBelt[0][0]>=1 and upperBelt[0][1]==0 :
        #벨트에 올리기
        upperBelt[0][1]=1

        #내구도 감소
        upperBelt[0][0]-=1
        if upperBelt[0][0]==0:
            countZero+=1

    if countZero>=K:
        print(ans)
        break

















