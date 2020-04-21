N,K=map(int,input().split())

def cheak(num):
    ans=0
    while(1):
        a=num//2
        b=num%2
        ans+=b
        num=a
        if num==0:
            break
    return ans


if K>=N:
    print(0)
else:
    i = N
    while(1):
        if cheak(i)<=K:
            print(i-N)
            break
        else:
            i+=1