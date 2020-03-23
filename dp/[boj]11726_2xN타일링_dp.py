n=int(input())
a=1
b=2
if n==1:
    print(1)
else:
    for i in range(n-2):
        temp=(a+b)%10007
        a=b
        b=temp
    print(b%10007)