for t in range(10):
    flatten=int(input())
    box=list(map(int,input().split()))
    for i in range(flatten):
        box[box.index(max(box))]-=1
        box[box.index(min(box))]+=1
    print(f"#{t+1} {max(box)-min(box)}")