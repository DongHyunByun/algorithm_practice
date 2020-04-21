import sys

N=int(input())
crane=list(map(int,input().split()))
M=int(input())
load=list(map(int,input().split()))
crane.sort(reverse=True)
load.sort(reverse=True)
craneSize=len(crane)
#화물이 더크면
if load[0]>crane[0]:
    print(-1)
    sys.exit()

time=0
while(load):
    indx=[] #이번타임에 옮길 물건들 index
    craneIndx=0
    size=len(load)
    for i in range(size):
        if craneIndx==craneSize:
            break
        if crane[craneIndx]>=load[i]:
            craneIndx+=1
            indx.append(i)
        else:
            continue

    #뒤에서부터 옮기기
    for i in range(len(indx)-1,-1,-1):
        del load[indx[i]]
    time+=1

print(time)