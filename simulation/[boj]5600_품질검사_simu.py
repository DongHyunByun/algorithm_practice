a,b,c=map(int,input().split())
N=int(input())
failL=[]
ansL=[2 for i in range(a+b+c+1)]
for i in range(N):
    temp=list(map(int,input().split()))
    if temp[3]==1:
        for j in range(3):
            ansL[temp[j]]=1
    else:
        failL.append(temp)

#하나남은건 고장으로 확정
for i in range(len(failL)):
    tempL=[]
    for j in range(3):
        if ansL[failL[i][j]] in [2,0]:
            tempL.append(failL[i][j])
    if len(tempL)==1:
        ansL[tempL[0]]=0

for i in range(1,a+b+c+1):
    print(ansL[i])
