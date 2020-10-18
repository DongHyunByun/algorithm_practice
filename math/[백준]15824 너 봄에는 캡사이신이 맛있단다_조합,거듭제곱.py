from itertools import combinations

def power(a,b,c):
    if b==0:
        return 1
    if b==1 :
        return a%c
    # 짝수이면 제곱
    if b%2==0:
        return power(a**2%c,b//2,c)
    else:
        return a*power(a**2%c,b//2,c)%c


N=int(input())
L=list(map(int,input().split()))
L.sort()
num=1000000007

#tosum[i] : 0부터 i까지의 합
toSum=[0 for i in range(N)]
toSum[0]=L[0]
for i in range(1,N):
    toSum[i]=toSum[i-1]+L[i]

#fromSum[i] : i에서 끝까지의 합
fromSum=[0 for i in range(N)]
fromSum[N-1]=L[N-1]
for i in range(N-2,-1,-1):
    fromSum[i]=fromSum[i+1]+L[i]

ans=0
for i in range(N-1):
    temp=(fromSum[i+1]-toSum[N-2-i])*power(2,i,num)
    ans+=temp
    ans=ans%num

print(ans)