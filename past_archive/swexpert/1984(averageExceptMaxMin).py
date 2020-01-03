for t in range(int(input())):
    L=list(map(int,input().split()))
    L.remove(max(L))
    L.remove(min(L))
    print(f"#{t+1} {round((sum(L)/len(L)))}")
