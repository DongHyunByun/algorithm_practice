def veriVertiHori(L):
    for i in range(9):
        if (len(set(L[i]))<9) or (len(set([row[i] for row in L]))<9):
            return 0
    return 1

def square(L):
    for i in range(0,9,3):
        for j in range(0,9,3):
            a=[]
            for k in range(3):
                for l in range(3):
                    a.append(L[i+k][j+l])
            if len(set(a))<9:
                return 0
    return 1
for t in range(int(input())):
    L=[]
    for i in range(9):
        L.append(list(map(int,input().split())))

    if veriVertiHori(L)==1:
        if square(L)==1:
            print(f"#{t+1} 1")
        else : 
            print(f"#{t+1} 0")
    else :
        print(f"#{t+1} 0")
         