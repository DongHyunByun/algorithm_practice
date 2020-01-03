for t in range(int(input())):
    L=input().split()
    if L.count(L[0])==2 : 
        if L[0]!=L[1]:
            print(f"#{t+1} {L[1]}")
        else:
            print(f"#{t+1} {L[2]}")
    else :
        print(f"#{t+1} {L[0]}")
