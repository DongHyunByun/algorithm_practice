from collections import deque
T=int(input())
reverseR={1:-1,-1:1}
# left자석, right자석 돌아가는지
def isRotate(left,right):
    if left[2]!=right[6]:
        return True
    else:
        return False

for t in range(T):
    k=int(input())
    L=[]
    order=[]
    # N:0, S:1
    for i in range(4):
        L.append(deque(list(map(int,input().split()))))
    # 시계방향:1, 반시계:-1
    ans=0
    for i in range(k):
        isRotateL=[[0,0] for i in range(4)] #[돌아가는지여부,방향]
        indx,rotate=map(int,input().split())
        indx-=1

        #해당 자석 확인
        isRotateL[indx][0]=1
        isRotateL[indx][1]=rotate
        #오른쪽 자석들 확인
        for i in range(indx+1,4):
            if isRotate(L[i-1],L[i]):
                isRotateL[i][0]=1
                if (i-indx)%2==0:
                    isRotateL[i][1]=rotate
                else:
                    isRotateL[i][1]=reverseR[rotate]
            else:
                break
        #왼쪽 자석들 확인
        for i in range(indx-1,-1,-1):
            if isRotate(L[i],L[i+1]):
                isRotateL[i][0]=1
                if (indx-i)%2==0:
                    isRotateL[i][1]=rotate
                else:
                    isRotateL[i][1]=reverseR[rotate]
            else:
                break

        #회전
        for i in range(4):
            if isRotateL[i][0]:
                if isRotateL[i][1]==1:
                    L[i].appendleft(L[i].pop())
                else:
                    L[i].append(L[i].popleft())
        '''
        print(isRotateL)
        print(L)
        '''
    ans=0
    for i in range(4):
        ans+=L[i][0]*(2**i)
    print("#%d %d"%(t+1,ans))






