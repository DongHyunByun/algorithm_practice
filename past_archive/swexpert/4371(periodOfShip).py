for t in range(int(input())):
    shipPeriodL=[]
    for n in range(int(input())):
        tem=int(input())-1
        if tem!=0:
            shipPeriodL.append(tem)
            for i in range(len(shipPeriodL)-1):
                if tem%shipPeriodL[i]==0:
                    shipPeriodL.pop()
                    break
    print(f"#{t+1} {len(shipPeriodL)}")
        
        
    


