for t in range(int(input())):
    s=input()
    for n in range(1,11):
        if (s[:n]==s[n:2*n]) :
            break
    print(f"#{t+1} {len(s[:n])}")