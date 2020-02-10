maxNum=123456*2
isPrime=[1 for i in range(maxNum+1)]

#에라토스테네스
def prime():
    isPrime[0]=isPrime[1]=0
    for i in range(2,maxNum+1):
        if isPrime[i]:
            for j in range(i*i,maxNum+1,i):
                isPrime[j]=0

def main():
    prime()
    while(1):
        a=int(input())
        if a==0:
            return
        print(sum(isPrime[a+1:2*a+1]))




main()