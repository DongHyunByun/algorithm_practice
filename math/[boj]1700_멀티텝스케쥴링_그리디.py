N,K=map(int,input().split())
L=list(map(int,input().split()))

myS=set([])
ans=0

for i in range(K):
    nowNum=L[i]
    #print(nowNum)

    # 콘센트 비어잇을때
    if len(myS)!=N:
        myS.add(nowNum)
    # 꽉차있고 빼야할때
    elif nowNum not in myS:
        # myS에서 nowNum으로 바꿀숫자를 찾는다
        ans+=1
        tempS=set(list(myS))
        for j in range(i+1,K):
            if len(tempS)==1:
                break
            num = L[j]
            if num in tempS:
                tempS.remove(num)

        myS.remove(list(tempS)[0])
        myS.add(nowNum)
    #print("콘센트현황", myS)
print(ans)


