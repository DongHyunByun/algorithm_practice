N,total=map(int,input().split())
oriL=[]
for i in range(N):
    oriL.append(int(input()))

L=sorted(oriL,key=abs)

# 가장왼쪽개미가 떨어지는 시간
leftTime=0
for i in range(N):
    if L[i]>0:
        leftTime=total-L[i]
        leftIndex=i
        break
# 가장 오른쪽 개미가 떨어지는 시간
rightTime=0
for i in range(N-1,-1,-1):
    if L[i]<0:
        rightTime=L[i]*(-1)
        rightIndex=i
        break

toRight=0
toLeft=0
for i in range(N):
    if L[i]:
        if L[i]>0:
            toRight+=1
        else:
            toLeft+=1

#왼쪽게 가장늦게 떨어질때
if leftTime>rightTime:
    print(oriL.index(L[toLeft])+1,leftTime)
#오른쪽게 가장 늦게 떨어질때
else:
    print(oriL.index(L[toLeft-1])+1,rightTime)