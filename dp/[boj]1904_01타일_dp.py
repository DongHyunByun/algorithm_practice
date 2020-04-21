a=1
b=1
N=int(input())
for i in range(1,N):
    temp=b
    b=(a+b)%15746
    a=temp
print(b)
