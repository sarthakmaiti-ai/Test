def binaryToDeci(binary):
    power=0
    result=0
    while(binary!=0):
        rem=binary%10
        result+=rem*2**power
        binary//=10
        power+=1
    return result

def deciToBin(decimal):
    if decimal==0:
        print(0)
        return
    binary=[]

    while(decimal!=0):
        binary.append(decimal%2)
        decimal=decimal//2

    i=0
    j=len(binary)-1
    while(i<j):
        binary[i],binary[j]=binary[j],binary[i]
        i+=1
        j-=1
    print(binary)


binary=1011
decimal=11
print(binaryToDeci(binary))
deciToBin(decimal)

