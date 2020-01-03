L=[]
for t in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a/b>c/d:
        L.append("ALICE")
    elif a/b<c/d:
        L.append("BOB")
    else:
        L.append("DRAW")

for i in range(len(L)):
    print(f"#{i+1} {L[i]}")