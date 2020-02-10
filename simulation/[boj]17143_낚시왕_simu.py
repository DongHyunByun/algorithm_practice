from copy import deepcopy

def returnSize(L):
    return L[2]

R,C,M=map(int,input().split())
L=[[[] for i in range(C+1)] for j in range(R+1)]
for i in range(M):
    temp=list(map(int,input().split()))
    L[temp[0]][temp[1]].append(list(temp[2:]))


ans=0
for j in range(1,C+1):
    '''
    for bo in range(R+1):
        print(L[bo])
    print()
    '''
    for i in range(1,R+1):
        # 상어 잡기
        if L[i][j]:
            ans+=L[i][j][0][2]
            L[i][j]=[]
            break
    #상어이동 시작
    newL = [[[] for i in range(C + 1)] for j in range(R + 1)]
    for r in range(1,R+1):
        for c in range(1,C+1):
            if L[r][c]:
                #print(r,c)
                s,d,z=L[r][c][0]
                startS=s
                if d==1:
                    if r-s>1:
                        newL[r-s][c].append([startS,d,z])
                    else:
                        s-=r-1
                        # 몫이 홀수면 방향은반대, 위치는 오른쪽부터
                        if (s//(R-1))%2==1:
                            newL[R-(s%(R-1))][c].append([startS,1,z])
                        # 몫이 짝수면 방향은
                        else:
                            newL[1+s%(R-1)][c].append([startS,2,z])
                elif d==2:
                    if r+s<R:
                        newL[r+s][c].append([startS,d,z])
                    else:
                        s-=R-r
                        # 몫이 홀수면 방향은반대, 위치는 오른쪽부터
                        if (s//(R-1))%2==1:
                            newL[R-(R-(s%(R-1)))+1][c].append([startS,2,z])
                        # 몫이 짝수면 방향은
                        else:
                            newL[R-(1+s%(R-1))+1][c].append([startS,1,z])
                elif d==3:
                    if c+s<C:
                        newL[r][c+s].append([startS,d,z])
                    #4랑 같은데 반대
                    else:
                        s-=C-c
                        # 몫이 홀수면 방향은반대, 위치는 오른쪽부터
                        if (s//(C-1))%2==1:
                            newL[r][C-(C-(s%(C-1)))+1].append([startS,3,z])
                        else:
                            newL[r][C-(1+s%(C-1))+1].append([startS,4,z])

                elif d==4:
                    if c-s>1:
                        newL[r][c-s].append([startS,d,z])
                    else:
                        s-=c-1
                        # 몫이 홀수면 방향은반대, 위치는 오른쪽부터
                        if (s//(C-1))%2==1:
                            newL[r][C-(s%(C-1))].append([startS,4,z])
                        else:
                            newL[r][1+s%(C-1)].append([startS,3,z])
                '''
                for a in range(R+1):
                    print(newL[a])
                '''

    # 잡아먹기
    for i in range(R+1):
        for j in range(C+1):
            if newL[i][j]:
                newL[i][j]=[max(newL[i][j],key=returnSize)]
    # 새로운 맵
    L=newL
    '''
    print("이동후 확인!")
    for i in range(R+1):
        print(newL[i])
    '''
print(ans)





