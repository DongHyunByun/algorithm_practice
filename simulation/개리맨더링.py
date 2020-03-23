from collections import deque
from itertools import combinations

N=int(input())
people=list(map(int,input().split()))
people.insert(0,0)
L=[[0]]
for _ in range(N):
    temp=list(map(int,input().split()))
    L.append(list(temp[1:]))


def isConnected(myL):
    A=deque(myL)
    connect=[A.popleft()]
    sizeA = len(A)
    #총 size-1번
    for _ in range(sizeA):
        #하나씩 확인
        nowSize=len(A)
        isCon=False
        for i in range(nowSize):
            temp=A.popleft()
            #connected와 연결되어있는가
            for j in connect:
                if temp in L[j]:
                    connect.append(temp)
                    isCon=True
                    break
                else:
                    continue
            if isCon:
                break
            else:
                A.append(temp)

        if not isCon:
            return False
    return True

ans=10000
forCom=[i for i in range(1,N+1)]

for i in range(1,N//2+1):
    comL=list(map(list,combinations(forCom,i)))
    #print(comL)
    for A in comL:
        B=list(forCom)
        #B리스트 만들기
        for a in A:
            B.remove(a)
        #연결됨
        if isConnected(A) and isConnected(B):
            sumA=0
            sumB=0
            for a in A:
                sumA+=people[a]
            for b in B:
                sumB+=people[b]
            if abs(sumA-sumB)<ans:
                ans=abs(sumA-sumB)

if ans==10000:
    print(-1)
else:
    print(ans)


