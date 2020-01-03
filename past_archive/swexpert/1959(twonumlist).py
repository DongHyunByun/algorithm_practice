def maxNum(long,short):
    max=0
    for i in range(len(long)-len(short)+1):
        ans=0
        for j in range(len(short)):
            ans=ans+long[j+i]*short[j]
        if (ans>max):
            max=ans
    return max

for t in range(int(input())):
    [N,M]=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    if N>M:
        print(f"#{t+1} {maxNum(A,B)}" )
    else :
        print(f"#{t+1} {maxNum(B,A)}" )

