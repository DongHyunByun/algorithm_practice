N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def returnSecond(L):
    return L[1]

L.sort(key=returnSecond)

preStart=L[N-1][1]-L[N-1][0]
for i in range(N-2,-1,-1):
    if preStart<L[i][1]:
        preStart=preStart-L[i][0]
    else:
        preStart=L[i][1]-L[i][0]

if preStart<0:
    print(-1)
else:
    print(preStart)