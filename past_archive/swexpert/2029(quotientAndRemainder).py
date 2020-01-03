T=int(input())

for i in range(T):
    a=list(map(int,input().split()))
    print("#"+str(i+1),a[0]//a[1],a[0]%a[1])