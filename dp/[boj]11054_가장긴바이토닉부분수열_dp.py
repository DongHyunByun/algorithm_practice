N=int(input())
L=list(map(int,input().split()))

'''
def search(nowindx,nextindx,dp):
    if nowindx==nextindx:
        ans.append(L[nowindx])
        return
    else:
        ans.append(L[nowindx])
        search(nextindx,dp[nextindx][1],dp)
'''

#최장증가수열
dpU=[[1,i] for i in range(N)]
for i in range(1,N):
    for j in range(i):
        if L[j]<L[i] and dpU[j][0]+1>dpU[i][0]:
            dpU[i][0]=dpU[j][0]+1
            dpU[i][1]=j
#최장감소수열
dpD=[[1,i] for i in range(N)]
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if L[j]<L[i] and dpD[j][0]+1>dpD[i][0]:
            dpD[i][0]=dpD[j][0]+1
            dpD[i][1]=j

size=[dpU[i][0]+dpD[i][0] for i in range(N)]
maxNum=max(size)
print(maxNum-1)
'''
indx=size.index(maxNum)
ans=[]
search(indx,dpU[indx][1],dpU)
ans.reverse()
ans.pop()
search(indx,dpD[indx][1],dpD)
print(dpU)
print(dpD)
print(*ans)
'''
