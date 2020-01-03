def eaOfChange(money):
    fiftyThou= money//50000
    left=money%50000
    tenThou=left//10000
    left=left%10000
    fiveThou=left//5000
    left=left%5000
    thou=left//1000
    left=left%1000
    fiveHund=left//500
    left=left%500
    hund=left//100
    left=left%100
    fifty=left//50
    left=left%50
    ten=left//10
    left=left%10
    return (f"{fiftyThou} {tenThou} {fiveThou} {thou} {fiveHund} {hund} {fifty} {ten}")

for t in range(int(input())):
    a = int(input())
    print(f"#{t+1}\n{eaOfChange(a)}")
