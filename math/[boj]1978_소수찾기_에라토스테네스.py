isPrime=[1 for i in range(1001)]
isPrime[0]=isPrime[1]=0
def aratos():
    for i in range(2,1001):
        if isPrime[i]:
            for j in range(i*i,1001,i):
                isPrime[j]=0

N=int(input())
L=list(map(int,input().split()))
aratos()
ans=0
for i in L:
    ans+=isPrime[i]
print(ans)