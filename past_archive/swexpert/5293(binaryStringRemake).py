def search(lastString,nowList):
    if nowList > L:
        return
    if nowList ==L:
        return nowList

    if lastString=="A":
        nowList[1]+=1
        return search("B",nowList)
    elif LastString=="B":
        nowList[2]+=1
        return search("C",nowList)

for t in range(int(input())):
    A,B,C,D=map(int,input().split())
    
