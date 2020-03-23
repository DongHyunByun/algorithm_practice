direct={"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
N,K=map(int,input().split())
move=input()

r=0
c=0
ans=1
for k in range(K):
    #이동
    to=move[k]
    r+=direct[to][0]
    c+=direct[to][1]

    #print("행과열은",r,c)
    isReverse=False
    #줄번호
    if r+c>=N:
        isReverse=True
        tempR=N-1-r
        tempC=N-1-c
        lineNum=tempR+tempC
    else:
        tempR=r
        tempC=c
        lineNum=r+c

    #짝수면
    if lineNum%2==0:
        startLoc=[lineNum,0]
        n=lineNum//2+1
        startValue=2*(n**2)-3*n+2
        value=startValue+tempC
        if isReverse:
            ans+=(N**2+1)-value
        else:
            ans+=value
    #홀수면
    else:
        startLoc=[0,lineNum]
        n=(lineNum+1)//2
        startValue=2*(n**2)-n+1
        value=startValue+tempR
        if isReverse:
            ans+=(N**2+1)-value
        else:
            ans+=value
    #print(value)
print(ans)