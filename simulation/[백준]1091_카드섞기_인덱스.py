from copy import deepcopy

N=int(input())

P=list(map(int,input().split()))
S=list(map(int,input().split()))

#카드덱
dq=[i for i in range(N)]

#현재 플레이어상태
player=[[] for i in range(3)]
for i in range(N):
    p=i%3
    player[p].append(i)

ini=deepcopy(player)

#목표값
target=[[] for i in range(3)]
for i in range(N):
    target[P[i]].append(i)

ans=0

while(1):
    if target==player:
        break
    if ans>=1 and player==ini:
        ans=-1
        break

    ans+=1

    #섞기
    temp = [-1 for i in range(N)]
    for i in range(N):
        c=dq[i]
        temp[S[i]]=c
    for i in range(N):
        dq[i]=temp[i]

    #나눠주기
    tempPlayer=[[] for i in range(3)]
    for i in range(N):
        p=i%3
        tempPlayer[p].append(dq[i])
    for i in range(3):
        tempPlayer[i].sort()

    player=deepcopy(tempPlayer)


print(ans)





