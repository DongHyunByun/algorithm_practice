from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
T=int(input())

for t in range(T):
    #입력
    h,w=map(int,input().split())
    L=[]
    L.append(["." for j in range(w+2)])
    for i in range(h):
        L.append(["."]+list(input())+["."])
    L.append(["." for j in range(w+2)])
    keyS=set()
    temp=input()
    if temp!="0":
        keyS=set(list(temp))
    '''
    for i in L:
        print(i)
    '''

    #찾기시작
    startR=0
    startC=0
    ans=0
    while(1):
        isFindKey=False
        visited=[[-1 for j in range(w+2)] for i in range(h+2)]
        visited[startR][startC]=1
        q=deque([[startR,startC]])
        while(q):
            r,c=q.popleft()
            for k in range(4):
                tempR=r+dR[k]
                tempC=c+dC[k]
                if 0<=tempR<h+2 and 0<=tempC<w+2 and visited[tempR][tempC]==-1:
                    if L[tempR][tempC]==".":
                        visited[tempR][tempC]=1
                        q.append([tempR,tempC])
                    elif L[tempR][tempC]=="$":
                        visited[tempR][tempC]=1
                        q.append([tempR,tempC])
                        ans+=1
                        L[tempR][tempC]="."
                    elif L[tempR][tempC]=="*":
                        continue
                    else:
                        #소문자(키획득)
                        if 97<=ord(L[tempR][tempC])<=122:
                            visited[tempR][tempC]=1
                            q.append([tempR,tempC])
                            if L[tempR][tempC] not in keyS:
                                isFindKey=True
                                keyS.add(L[tempR][tempC])
                                #다음시작위치
                                startR=tempR
                                startC=tempC
                            L[tempR][tempC] = "."
                        #대문자(문)
                        else:
                            if chr(ord(L[tempR][tempC])+32) in keyS:
                                visited[tempR][tempC]=1
                                q.append([tempR,tempC])
                                L[tempR][tempC]="."
        if not isFindKey:
            break

    print(ans)