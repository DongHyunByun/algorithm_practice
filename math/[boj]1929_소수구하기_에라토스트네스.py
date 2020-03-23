M, N = map(int, input().split())
isPrime=[1 for i in range(N+1)]
isPrime[0]=0
isPrime[1]=0

def aretos():
    for i in range(2,N+1):
        if isPrime[i]==1:
            for j in range(i*i,N+1,i):
                isPrime[j]=0

def main():
    aretos()
    for i in range(M,N+1):
        if isPrime[i]:
            print(i)


main()
