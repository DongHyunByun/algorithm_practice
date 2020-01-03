T=int(input())


#문자열로 입력받음
def isAbleDate(a) :
    if (a[4:6] in ['01','03','05','07','08','10','12']) and (int(a[6:])<=31):
        return a[0:4]+"/"+a[4:6]+"/"+a[6:]
    elif ( a[4:6] in ['04','06','09','11']) and (int(a[6:])<=30):
        return a[0:4]+"/"+a[4:6]+"/"+a[6:]
    elif (a[4:6]=='02') and (int(a[6:])<=28):
        return a[0:4]+"/"+a[4:6]+"/"+a[6:]
    else :
        return -1

for i in range(T):
    print("#"+str(i+1),isAbleDate(input()))