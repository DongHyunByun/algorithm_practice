for t in range(int(input())):
    card=input()
    S=set()
    D=set()
    H=set()
    C=set()
    for i in range(0,len(card),3):
        if card[i]=="S":
            S.add(card[i+1:i+3])
        elif card[i]=="D":
            D.add(card[i+1:i+3])
        elif card[i]=="H":
            H.add(card[i+1:i+3])
        else:
            C.add(card[i+1:i+3])
    if (int(len(card)/3))!=len(S)+len(D)+len(H)+len(C):
        print(f"#{t+1} ERROR")
    else :
        print(f"#{t+1} {13-len(S)} {13-len(D)} {13-len(H)} {13-len(C)}")

