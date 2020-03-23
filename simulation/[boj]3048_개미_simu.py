sizeA,sizeB=map(int,input().split())
A=input()
B=input()
T=int(input())

listA=list(A)
listB=list(B)

if T<sizeA:
    ans=""
    for _ in range(sizeA-T):
        ans+=listA.pop()
    for t in range(T,0,-1):
        if listB:
            ans+=listB.pop(0)
        ans+=listA.pop()

    for i in listB:
        ans+=i


else:
    ans=""
    for t in range(T,0,-1):
        if listB:
            ans+=listB.pop(0)
        if t<=sizeA :
            ans+=listA.pop()
    if listB:
        for i in listB:
            ans+=i

print(ans)