N=int(input())
L=[]
for i in range(N):
    temp=input()
    size=len(temp)

    nowSum=0
    for alpa in temp:
        try:
            nowSum+=int(alpa)
        except:
            pass
    L.append([size,nowSum,temp])

L.sort()

for i in range(N):
    print(L[i][2])