def solution(name):
    ans=0
    point=0 #현재 포인트
    nameL=list(name)

    #A의 개수
    numOfA=0
    for i in range(1,len(nameL)):
        if nameL[i]=="A":
            numOfA+=1



    for i in range(len(name)-numOfA):

        distanse=ord(nameL[point])-ord("A")
        if distanse<=13:
            ans+=distanse
        else:
            ans+=26-distanse
        nameL[point]=0


        if i==len(name)-numOfA-1:
            break
        moveL=1
        #왼쪽으로 이동
        while(nameL[point-moveL]==0 or nameL[point-moveL]=="A"):
            moveL+=1

        #오른쪽으로 이동 
        moveR=1
        temp=point
        while(1):
            if (temp+moveR)>len(nameL)-1:
                temp-=len(nameL)
            if (nameL[temp+moveR]==0 or nameL[temp+moveR]=="A"):
                moveR+=1
            else:
                break

        if (moveL>=moveR):
            if point+moveR>len(nameL)-1:
                point=point+moveR-len(nameL)
            else:
                point=point+moveR
            ans+=moveR
        else:
            if  point-moveL<0:
                point=point-moveL+len(nameL)
            else:
                point=point-moveL
            ans+=moveL
        print(i+1,"번째",nameL,ans)
    print(len(nameL)-numOfA-1,"번째",nameL,ans)
    return ans