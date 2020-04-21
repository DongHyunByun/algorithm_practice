N=int(input())
L=list(map(int,input().split()))
S=int(input())

for i in range(N):
    #현재위치에서 S개만큼
    maxNum=max(L[i:i+S+1])
    maxIndx=L.index(maxNum)
    S-=(maxIndx-i)

    del L[maxIndx]
    L.insert(i,maxNum)

    if S==0:
        break

print(*L)
