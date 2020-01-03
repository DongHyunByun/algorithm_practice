def solution(s):
    sL=list(s)
    isDouble=True
    while(isDouble):
        isDouble=False
        for i in range(len(sL)-1):
            if sL[i]==sL[i+1]:
                del sL[i:i+2]
                isDouble=True
                break
    if sL:
        return 0
    else:
        return 1