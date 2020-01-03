for t in range(int(input())):
    input().split()
    L=[]
    L.extend(input().split())
    dict=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    countL=[]
    for i in dict:
        countL.append(L.count(i))
    print(f"#{t+1}")
    for j in range(len(dict)):
        for k in range(countL[j]):
            print(dict[j],end=" ")
                