N,M,K=map(int,input().split())
noteBook=[[0 for j in range(M)] for i in range(N)]

def attach(stick,sizeR,sizeC):
    #i,j에 붙일 수 있는지 확인
    for i in range(N-sizeR+1):
        for j in range(M-sizeC+1):
            isPossible=True
            for stickI in range(sizeR):
                for stickJ in range(sizeC):
                    if stick[stickI][stickJ] and noteBook[i+stickI][j+stickJ]:
                        isPossible=False
                        break
                if not isPossible:
                    break
            #붙일수 있으면 붙이기
            if isPossible:
                for stickI in range(sizeR):
                    for stickJ in range(sizeC):
                        if not noteBook[i+stickI][j+stickJ]:
                            noteBook[i+stickI][j+stickJ]=stick[stickI][stickJ]
                return True
    return False

#k번째 스티커 부텨보기
for k in range(K):
    '''
    print("노트북상태는")
    for x in noteBook:
        print(x)
    print(k,"번째 스티커 시작")
    '''
    R,C=map(int,input().split())
    stick=[]
    for i in range(R):
        stick.append(list(map(int,input().split())))
    for i in range(4):
        '''
        print(i+1,"회전!")
        for x in stick:
            print(x)
        '''
        #붙일 수 있으면 붙치고 끝내기
        if attach(stick,R,C):
            break
        #못붙이면 돌리고 다음수행
        else:
            stick = list(map(list, zip(*stick[::-1])))
            R,C=C,R


print(sum([sum(i) for i in noteBook]))


