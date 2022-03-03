dR=[0,0,-1,1]
dC=[1,-1,0,0]

N,M = map(int,input().split())

L=[]
for i in range(N):
    L.append(list(input()))

ans = 11

def find_start(L):
    loc = []
    for i in range(N):
        for j in range(M):
            if L[i][j]=="o":
                L[i][j]="."
                loc.append((i,j))

    return loc

def dfs(first,second,cnt):
    global ans

    # 10번눌렀는데도 안떨어졌다면 종료
    if cnt==10:
        return
    # print(first,second)

    for k in range(4):
        next_first_r = first[0] + dR[k]
        next_first_c = first[1] + dC[k]
        next_first_possible = 1 #0:떨어짐 1:이동가능

        next_second_r = second[0] + dR[k]
        next_second_c = second[1] + dC[k]
        next_second_possible = 1 #0:떨어짐 1:이동가능

        if 0<=next_first_r<N and 0<=next_first_c<M:
            if L[next_first_r][next_first_c]==".": # 이동가능
                next_first_possible = 1
            else: # 이동불가능, 원래자리로
                next_first_r = first[0]
                next_first_c = first[1]
        else: # 떨어짐
            next_first_possible = 0

        if 0<=next_second_r<N and 0<=next_second_c<M:
            if L[next_second_r][next_second_c]==".":
                next_second_possible = 1
            else:
                next_second_r = second[0]
                next_second_c = second[1]
        else:
            next_second_possible = 0

        # print(next_first_possible,next_second_possible)
        # 결과
        if next_first_possible==0 and next_second_possible==0: #둘다 떨어짐
            continue
        elif (next_first_possible==1 and next_second_possible==0) or (next_first_possible==0 and next_second_possible==1): #하나만 떨어짐
            if cnt+1<ans:
                ans=cnt+1
            continue
        else: # 둘다 안떨어짐
            if first[0]==next_first_r and first[1]==next_first_c and second[0]==next_second_r and second[1]==next_second_c:
                continue
            else:
                dfs((next_first_r,next_first_c),(next_second_r,next_second_c),cnt+1)



first,second = find_start(L)
dfs(first,second,0)

if ans==11:
    print(-1)
else:
    print(ans)
