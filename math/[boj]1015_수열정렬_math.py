N=int(input())
B=list(map(int,input().split()))
temp=[] # temp[i]=[값,p의 인덱스] , i는 p[p인덱스]의 값
for i in range(N):
    temp.append([B[i],i])
temp.sort()

ans=[0 for i in range(N)]
for i in range(N):
    ans[temp[i][1]]=i
print(*ans)

