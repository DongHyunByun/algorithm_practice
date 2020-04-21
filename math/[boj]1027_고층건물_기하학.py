N=int(input())
L=list(map(int,input().split()))

countL=[[0 for j in range(N)] for i in range(N)]


for i in range(N):
    tilt=-9876543210
    for j in range(i+1,N):
        #보인다!
        if tilt*(j-i)+L[i]<L[j]:
            countL[i][j]=1
            tilt=(L[j]-L[i])/(j-i)
        #안보인다
        else:
            countL[i][j]=0

ans=0
for j in range(N):
    rowSum=sum(countL[j])
    colSum=sum([countL[i][j] for i in range(N)])
    total=rowSum+colSum
    if ans<total:
        #print(j,"번째")
        ans=total
print(ans)