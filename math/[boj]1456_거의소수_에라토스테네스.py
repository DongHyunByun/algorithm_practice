import math
a,b=map(int,input().split())
toB=int(math.sqrt(b))
isPrime=[1 for i in range(toB+1)]
isPrime[0]=isPrime[1]=0

def aratos():
    global ans
    for i in range(2,toB+1):
        if isPrime[i]:
            #print(i,"는 소수")
            # a<=i^n<=b인 값을 구한다
            n=2
            while(i**n<=b):
                if i**n>=a:
                    #print(i**n)
                    ans+=1
                n+=1
            for j in range(i*i,toB+1,i):
                isPrime[j]=0

ans=0
aratos()
print(ans)