def second(L):
    return L[1]

#r,c의 kind가 존립할수 있는가?
def removeCheak(r,c,kind):
    global L,R,C
    if L[r][c][kind]==0:
        return True
    #기둥
    if kind==0:
        if (0<=r-1 and L[r-1][c][1]) or (0<=c-1 and L[r][c-1][0]) or (L[r][c][1]):
            return True
        else:
            return False
    #보
    else:
        if (0<=c-1 and L[r][c-1][0]) or (0<=c-1 and L[r+1][c-1][0]) or (0<=r-1 and L[r-1][c][1] and L[r+1][c][1]):
            return True
        else:
            return False

def solution(n, build_frame):
    global L,R,C
    R=max(build_frame)[0]
    C=max(build_frame,key=second)[1]
    L=[[[0,0] for j in range(C+10)] for i in range(R+10)]
    ans=[]
    for build in build_frame:
        #print(ans)
        r,c,t,b=build
        #print(build)

        #있는데 건설하는 경우 or 없는데 삭제하는 경우는 통과
        if (b==1 and L[r][c][t]) or (b==0 and L[r][c][t]==0):
            continue

        #기둥
        if t==0:
            #삭제
            if b==0:
                #삭제하고
                L[r][c][t]=0
                #모두 존립가능하면 삭제
                if removeCheak(r,c+1,0) and removeCheak(r-1,c+1,1) and removeCheak(r,c+1,1):
                    ans.remove([r, c, t])
                else:
                    L[r][c][t] = 1
            #설치
            else:
                # 1.바닥
                if c==0:
                    L[r][c][t]=1
                    ans.append([r, c, t])
                # 2.기둥위
                elif L[r][c-1][0]:
                    L[r][c][t]=1
                    ans.append([r, c, t])
                # 3.보끝
                elif L[r-1][c][1] or L[r][c][1]:
                    L[r][c][t]=1
                    ans.append([r,c,t])
        #보
        else:
            #삭제
            if b==0:
                #삭제하고
                L[r][c][t]=0
                #모두 존립가능하면 진짜삭제
                if removeCheak(r-1,c,1) and removeCheak(r,c,0) and removeCheak(r+1,c,0) and removeCheak(r+1,c,1):
                    ans.remove([r, c, t])
                else:
                    L[r][c][t] = 1
            #설치
            else:
                # 1. 기둥있을때
                if L[r][c-1][0] or L[r+1][c-1][0]:
                    L[r][c][t]=1
                    ans.append([r, c, t])
                # 2. 양쪽에 보가있을때
                elif L[r-1][c][1] and L[r+1][c][1]:
                    L[r][c][t]=1
                    ans.append([r, c, t])
    ans.sort()
    return ans


print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))