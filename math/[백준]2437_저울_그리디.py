N=int(input())
L=list(map(int,input().split()))
L.sort()

nowSum=1
for i in range(N):
    if nowSum<L[i]:
        break
    nowSum+=L[i]

print(nowSum)

