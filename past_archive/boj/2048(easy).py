from collections import deque
from copy import deepcopy
N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
ans=0


def move(L,num):
    #위로
    if num==0:
        for j in range(N):
            tempL=[]
            count=0
            while(count<N):
                if L[count][j]==0:
                    count+=1
                    continue
                if count==N-1 :
                    tempL.append(L[count][j])
                    break
                else:
                    a=1
                    while (count+a<N):
                        if L[count+a][j]==0:
                            if count+a==N-1:
                                tempL.append(L[count][j])
                                count=N
                                break
                            else:
                                a+=1
                                continue
                        else:
                            if L[count][j]==L[count+a][j]:
                                tempL.append(L[count][j]*2)
                                count+=a+1
                            else:
                                tempL.append(L[count][j])
                                count+=a
                            break
            for i in range(len(tempL)):
                L[i][j]=tempL[i]
            for i in range(len(tempL),N):
                L[i][j]=0
       

    #아래로
    elif num==3:
        for j in range(N):
            tempL=[]
            count=N-1
            while(count>-1):
                if L[count][j]==0:
                    count-=1
                    continue
                if count==0 :
                    tempL.append(L[count][j])
                    break
                else:
                    a=1
                    while (count-a>-1):
                        if L[count-a][j]==0:
                            if count-a==0:
                                tempL.append(L[count][j])
                                count=-1
                                break
                            else:
                                a+=1
                                continue
                        else:
                            if L[count][j]==L[count-a][j]:
                                tempL.append(L[count][j]*2)
                                count-=a+1
                            else:
                                tempL.append(L[count][j])
                                count-=a
                            break

            for i in range(len(tempL)):
                L[N-1-i][j]=tempL[i]
            for i in range(N-len(tempL)):
                L[i][j]=0
    #왼쪽
    if num==1:
        for i in range(N):
            tempL=[]
            count=0
            while(count<N):
                if L[i][count]==0:
                    count+=1
                    continue
                if count==N-1 :
                    tempL.append(L[i][count])
                    break
                else:
                    a=1
                    while (count+a<N):
                        if L[i][count+a]==0:
                            if count+a==N-1:
                                tempL.append(L[i][count])
                                count=N
                                break
                            else:
                                a+=1
                                continue
                        else:
                            if L[i][count]==L[i][count+a]:
                                tempL.append(L[i][count]*2)
                                count+=a+1
                            else:
                                tempL.append(L[i][count])
                                count+=a
                            break
            for j in range(len(tempL)):
                L[i][j]=tempL[j]
            for j in range(len(tempL),N):
                L[i][j]=0
    #오른쪽
    if num==2:
        for i in range(N):
            tempL=[]
            count=N-1
            while(count>-1):
                if L[i][count]==0:
                    count-=1
                    continue
                if count==0 :
                    tempL.append(L[i][count])
                    break
                else:
                    a=1
                    while (count-a>-1):
                        if L[i][count-a]==0:
                            if count-a==0:
                                tempL.append(L[i][count])
                                count=-1
                                break
                            else:
                                a+=1
                                continue
                        else:
                            if L[i][count]==L[i][count-a]:
                                tempL.append(L[i][count]*2)
                                count-=a+1
                            else:
                                tempL.append(L[i][count])
                                count-=a
                            break
            for j in range(len(tempL)):
                L[i][N-1-j]=tempL[j]
            for j in range(N-len(tempL)):
                L[i][j]=0
    '''
    for i in L:
        print(i)
    print()
    '''
    
'''
def dfs(L,num):
    global ans
    for i in range(4):
        tempL=deepcopy(L)
        move(tempL,i)
        num+=1
        if num==5:
            maxNum=max(map(max,tempL))
            if maxNum>ans:
                ans=maxNum

        elif tempL!=L:
            dfs(tempL,num)
'''


stack=[[L,0]]
while stack:
    temp=stack.pop()
    for i in range(4):
        copiedL=deepcopy(temp[0])
        move(copiedL,i)
        
        maxNum=max(map(max,copiedL))
        if maxNum>ans:
            ans=maxNum
        if temp[1]==4:
            continue
        elif copiedL!=temp[0]:
            stack.append([copiedL,temp[1]+1])

print(ans)

