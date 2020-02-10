money=1000-int(input())

moneyL=[500,100,50,10,5,1]

ans=0
for i in range(6):
    while(money>=moneyL[i]):
        money-=moneyL[i]
        ans+=1
    if money==0:
        break

print(ans)


