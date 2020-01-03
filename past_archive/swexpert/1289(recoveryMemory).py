for t in range(int(input())):
    memory=input()
    ans=0
    lastString="0"
    for i in range(len(memory)):
        if memory[i]!=lastString:
            ans+=1
            lastString=memory[i]
    print(f"#{t+1} {ans}")