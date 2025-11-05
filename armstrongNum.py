def isArmstrong(num):
    n=len(str(num))
    sum=0
    temp2=num
    while(temp2!=0):
        rem=temp2%10
        sum+=rem**n
        temp2//=10
    return sum==num

num=153
print(isArmstrong(num))
