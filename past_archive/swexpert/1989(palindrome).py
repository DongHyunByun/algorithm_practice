for i in range(int(input())):
    word=input()
    if word==word[::-1]:
        print(f"#{i+1} 1")
    else :
        print(f"#{i+1} 0")