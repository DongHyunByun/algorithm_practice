import sys

def aratos():
    for i in range(2,N+1):
        if isPrime[i]:
            primeL.append(i)
            for j in range(i*i,N+1,i):
                isPrime[j]=0


N=int(input())
isPrime = [1 for i in range(N + 1)]
isPrime[0] = isPrime[1] = 0
primeL = []
aratos()
size=len(primeL)

def goldbach(num):
    for i in range(size):
        for j in range(size):
            sumOfNum=primeL[i]+primeL[j]
            if sumOfNum==num:
                ans.extend([primeL[i],primeL[j]])
                return
            elif sumOfNum>num:
                break


if N<8:
    print(-1)
else:
    #짝수이면
    if N%2==0:
        ans=[2,2]
        N-=4
        goldbach(N)
        print(*ans)
    #홀수이면
    else:
        ans=[2,3]
        N-=5
        goldbach(N)
        print(*ans)