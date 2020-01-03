def solution(numOfChange,N,indx):
    global ans
    #indx가 마지막 까지 왔다면
    if indx==size-1:
        #중복이 있다면 최댓값 가능
        if len(set(N))<size:
            ans=int("".join(N))
            return
        #중복이 없다면 (홀수이면 최대-1번쨰, 짝수면 최대)
        if numOfChange<maxChange:
            copyL=list(N)
            copyL[size-2],copyL[size-1]=copyL[size-1],copyL[size-2]
            solution(numOfChange+1,copyL,indx)
        else:
            temp=int("".join(N))
            if temp>ans:
                ans=temp
        return

    maxNum=max(N[indx:])
    #마지막 교체
    if (numOfChange==maxChange):
        temp=int("".join(N))
        if temp>ans:
            ans=temp
        return

    #맨앞이 최댓값일때
    if (maxNum==N[indx]):
        solution(numOfChange,N,indx+1)
    else:
        for i in range(indx+1,size):
            if (N[i]==maxNum):
                copyL=list(N)
                copyL[i],copyL[indx]=copyL[indx],copyL[i]
                solution(numOfChange+1,copyL,indx+1)

for t in range(int(input())):
    N,maxChange=input().split()
    maxChange=int(maxChange)
    N=list(N)
    size=len(N)
    ans=-1
    solution(0,N,0)
    print(f"#{t+1} {ans}")

