def cheak(M):
    sizeM=len(M)
    preH=M[0]
    indx=1
    isUsed=[0 for i in range(sizeM)]
    while(indx!=sizeM):
        # 하나작아질 때(뒤에 경사로 놓기)
        if preH==M[indx]+1 :
            #print("작아진다 인덱스는 ",indx)
            # 남은자리(indx 뒤에가) L만큼없어
            if indx>sizeM-L:
                return False
            else:
                # L만큼 평평한가?
                num=M[indx]
                #print("첫숫자는", num)
                isUsed[indx]=1
                for i in range(1,L):
                    #print(i,"번이동했더니",M[indx+i])
                    if num!=M[indx+i]:
                        return False
                    else:
                        isUsed[indx+i]=1
                # 평평하면 통과
                indx+=L
                preH=M[indx-1]
                #print("바뀐indx는",indx,"이전높이는",preH)
        # 하나 커질 때(앞에 경사로 놓기)
        elif preH==M[indx]-1:
            # 남은자리(indx 앞에가) L만큼없어
            if indx<L:
                return False
            else:
                # L만큼 평평한가?
                if isUsed[indx-1]==0:
                    num=M[indx-1]
                    isUsed[indx-1]=1
                else:
                    return False
                for i in range(2,L+1):
                    if num!=M[indx-i] or isUsed[indx-i]==1:
                        return False
                    else:
                        isUsed[indx-i]=1
                # 평평하면 통과
                indx+=1
                preH = M[indx-1]
        # 같을때
        elif preH==M[indx]:
            indx+=1
        # 두개이상차이날때
        else:
            return False
    return True

if __name__=='__main__':
    N,L=map(int,input().split())
    myMap=[]
    for i in range(N):
        myMap.append(list(map(int,input().split())))
    ans=0

    # 가로줄 체크
    for road in myMap:
        if (cheak(road)):
            ans+=1

    # 세로줄 체크
    for j in range(N):
        #print("현재 col은",j)
        tempL=[]
        for i in range(N):
            tempL.append(myMap[i][j])
        if (cheak(tempL)):
            ans+=1
    print(ans)


