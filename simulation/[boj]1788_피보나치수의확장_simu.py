n=int(input())

if n==0:
    print(0)
    print(0)
elif abs(n)==1:
    print(1)
    print(1)
else:
    a = 0
    b = 1
    for i in range(abs(n)-1):
        c=(a+b)%1000000000
        a=b
        b=c
    #양수면?
    if n>0:
        print(1)
        print(c%1000000000)
    #음수면?
    else:
        if n%2==0:
            print(-1)
        else:
            print(1)
        print(c%1000000000)