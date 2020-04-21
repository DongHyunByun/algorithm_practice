N=int(input())
L=[]
for i in range(N):
    L.append(list(input()))

#초기화
INF=9876543210
floid=[[INF for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            floid[i][j]=0
        elif L[i][j]=="Y":
            floid[i][j]=1
#초기화
for k in range(N):
    for i in range(N):
        for j in range(N):
            if floid[i][k]+floid[k][j]<floid[i][j]:
                floid[i][j]=floid[i][k]+floid[k][j]

ans=0
for i in range(N):
    cnt=0
    for j in range(N):
        if 1<=floid[i][j]<=2:
            cnt+=1
    if cnt>ans:
        ans=cnt
print(ans)
