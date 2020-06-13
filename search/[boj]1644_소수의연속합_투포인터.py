N=int(input())

isPrime=[1 for i in range(N+1)]
isPrime[0]=isPrime[1]=0
primeL=[]
def aratos():
    for i in range(2,N+1):
        if isPrime[i]:
            primeL.append(i)
            for j in range(i*i,N+1,i):
                isPrime[j]=0

def twoPoint():
    s=0
    e=0
    cnt=0
    S=0
    while(1):
        if S==N:
            cnt+=1
            e+=1
            if e==size+1:
                return cnt
            S+=primeL[e-1]
        elif S<N:
            e+=1
            if e==size+1:
                return cnt
            S+=primeL[e-1]
        else:
            S-=primeL[s]
            s+=1


aratos()
size=len(primeL)
print(twoPoint())