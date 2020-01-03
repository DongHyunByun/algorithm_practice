L=[]
for t in range(int(input())):
    num=input()
    while len(num)!=1:
        sumDigit=0
        for i in num:
            sumDigit+=int(i)
        num=str(sumDigit)
    L.append(num)


for t in range(len(L)):
    print(f"#{t+1} {L[t]}")