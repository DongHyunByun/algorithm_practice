import sys

N=int(input())
L=list(map(int,input().split()))
M=int(input())

size=len(L)
dp=[[1 for j in range(size)] for i in range(size)]

for j in range(1,size):
    for k in range(size-j):
        #시작점은 i,j
        if L[j+k]==L[k] and dp[k+1][j+k-1]:
            dp[k][j+k]=1
        else:
            dp[k][j+k]=0
'''
for i in range(size):
    print(dp[i])
'''
for i in range(M):
    S,E=map(int,sys.stdin.readline().rstrip().split())
    print(dp[S-1][E-1])