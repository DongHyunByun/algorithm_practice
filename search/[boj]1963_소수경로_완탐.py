from collections import deque

isPrime=[1 for i in range(10000)]
def aratos():
    isPrime[0]=isPrime[1]=0
    for i in range(2,10000):
        if isPrime[i]:
            for j in range(i*i,10000,i):
                isPrime[j]=0

aratos()
for i in range(1000):
    isPrime[i]=0

T=int(input())
for t in range(T):
    #방문되면 0으로 바뀜
    visited=list(isPrime)
    a,b=map(int,input().split())
    q=deque([[a,0]])
    visited[a]=0
    ans="Impossible"
    while(q):
        temp=q.popleft()
        num=temp[0]
        cnt=temp[1]
        if num==b:
            ans=cnt
            break

        L=list(str(num))
        for digit in range(4):
            copiedL=list(L)
            digitNum=copiedL[digit]
            for i in range(1,10):
                copiedL[digit]=str((int(digitNum)+i)%10)
                number=int("".join(copiedL))
                if visited[number]==1:
                    visited[number]=0
                    q.append([number,cnt+1])
    print(ans)

