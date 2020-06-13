N=int(input())
L=[]
returnUp=[5,3,4,1,2,0]

for i in range(N):
    L.append(list(map(int,input().split())))

ans=0
for i in range(1,7):
    nowSum=0
    #print(i,"가 밑에일때")
    up=i #아래 주사위의 윗면의 숫자
    for j in range(N):
        downAlpa=L[j].index(up)
        upAlpa=returnUp[downAlpa]

        indexL=[0,1,2,3,4,5]
        indexL.remove(downAlpa)
        indexL.remove(upAlpa)

        maxNum=max([L[j][k] for k in indexL])
        up=L[j][upAlpa]
        #print(j,"번 최대수는 ",maxNum)
        nowSum+=maxNum
    if nowSum>ans:
        ans=nowSum
print(ans)