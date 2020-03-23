n=int(input())
sang=[]
gun=[]
for i in range(n):
    sang.append(int(input()))
for i in range(1,2*n+1):
    if i not in sang:
        gun.append(i)

L=[sorted(sang),sorted(gun)]
preNum=0
num=0
while(1):
    p=L[num%2]
    noCard=True
    for i in range(len(p)):
        if preNum<p[i]:
            preNum=p[i]
            del p[i]
            noCard=False
            break

    #낼카드없다면
    if noCard:
        preNum=0
    #낼카드있다면
    else:
        if not p:
            break
    num+=1

print(len(L[1]))
print(len(L[0]))





