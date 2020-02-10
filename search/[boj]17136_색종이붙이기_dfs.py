from collections import deque
from copy import deepcopy
L=[]
for i in range(10):
    L.append(list(map(int,input().split())))

stack=deque([[[0 for i in range(5)],L,0]])

ans=26

def isAllZero(L):
    for i in L:
        if sum(i)!=0:
            return False
    return True

while(stack):
    temp=stack.pop()
    used=temp[0]
    copiedL=temp[1]
    sumAns=sum(used)
    '''
    print("--------------")
    print(used)
    print(num)
    for i in copiedL:
        print(i)
    print("--------------")
    '''

    if sumAns>=ans:
        continue


    #모두0이면 통과
    if isAllZero(copiedL):
        if sumAns<ans:
            ans=sumAns
        continue
    else:
        for i in range(10):
            for j in range(10):
                #해당지점 찾음
                isFind=False
                if copiedL[i][j]==1:
                    isFind=True
                    # 1*1 ~ 5*5
                    for k in range(1,6):
                        if used[k-1]<5 and i+k-1<10 and j+k-1<10:
                            isPossible=True
                            for l in range(k):
                                for m in range(k):
                                    if copiedL[i+l][j+m]==0:
                                        isPossible=False
                                        break
                                if not isPossible:
                                    break
                            if isPossible:
                                tempUsed = list(used)
                                tempL = deepcopy(copiedL)
                                tempUsed[k-1]+=1
                                for l in range(k):
                                    for m in range(k):
                                        tempL[i+l][j+m]=0
                                '''
                                print("처리결과")
                                for z in tempL:
                                    print(z)
                                print(tempUsed,num+1)
                                '''
                                stack.append([tempUsed,tempL])
                    break
            if isFind:
                break




if ans==26:
    print(-1)
else:
    print(ans)